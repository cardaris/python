"""
Filename       : Progress.py
Author         : Alexandros M. Cardaris <cardaris@pm.me>
License        : GPL-3.0
Date Created   : 2019-06-10
Date Modified  : 2019-06-10
Version		   : 1.0.0
Python Version : 3.6+
"""

import numbers

class Progress:
	def __init__(self, target=None, interval=1, verbose=False):
		"""
		This is a progress init function
		:param target: the target number to reach
		:param interval: printing the progress percentange every interval number
		:param verbose: an boolean flag for verbose progress printing
		:returns: True in case of success and False otherwise
		:raises NameError: raises an exception in case of empty target
		:raises TypeError: raises an exception in case of invalid target
		:raises ValueError: raises an exception in case of invalid target
		"""	
		
		if (target == None or interval == None):
			raise NameError("Missing a required argument")
		elif (not isinstance(target, numbers.Number) or not isinstance(interval, numbers.Number)):
			raise TypeError("A required parameter is not a number")
		elif (target <= 0 or interval <= 0 or interval > 100):
			raise ValueError("A required parameter has an invalid value")

		self.target = target
		self.interval = interval
		self.verbose = verbose
		self.intervals = []
		self.Reset()

		return
	
	def Reset(self):
		"""
		This function sets the progress to zero		
		:returns: None
		"""
		
		self.value = 0.0
		self.current = 0
		del self.intervals[:]

		for i in range(0, 100, self.interval):
			self.intervals.append(i)
			
		if (self.intervals[-1] != 100):
			self.intervals.append(100)

		return
	
	def Increment(self):
		"""
		This function increments the progress		
		:returns: None
		"""

		self.current += 1
		self.value = round(self.current * 100 / self.target, 1)
		
		while (len(self.intervals) > 0 and self.value >= self.intervals[0]):
			if (self.verbose):
				print("Progress: {0}%\t {1} out of {2}".format(self.intervals[0], self.current, self.target))
			else:
				print("Progress: {0}%".format(self.intervals[0]))
			del self.intervals[0]
		
		return


"""
An example program using the Progress class:
--------------------------------------------
sum = 1
target = 500
progress = Progress(target, 20, True)

for i in range(0, target):
	sum += i
	progress.Increment()

print("The total sum is {0}.".format(sum))
del progress
"""

"""
The output of the above program:
--------------------------------
Progress: 0%	 1 out of 500
Progress: 20%	 100 out of 500
Progress: 40%	 200 out of 500
Progress: 60%	 300 out of 500
Progress: 80%	 400 out of 500
Progress: 100%	 500 out of 500

The total sum is 124751.
"""