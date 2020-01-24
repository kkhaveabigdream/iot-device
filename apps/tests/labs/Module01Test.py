"""
Test class for all requisite Module01 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""

import unittest
from labs.module01.SystemCpuUtilTask import SystemCpuUtilTask
from labs.module01.SystemMemUtilTask import SystemMemUtilTask

class Module01Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.c=SystemCpuUtilTask()
		self.m=SystemMemUtilTask()
	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		pass
	
	"""
	getDataFromSensor() function returns a float value representing the on-demand CPU utilization
	passing values will be anything between 0.0 and 100.0	
	"""
	def testSystemCpuUtil(self):
		assert self.c.getDataFromSensor()>0 and self.c.getDataFromSensor()<100
	
	"""
	getDataFromSensor() function returns a float value representing the on-demand Memory utilization
	passing values will be anything between 0.0 and 100.0	
	"""	
	def testSystemMemUtil(self):
		assert self.m.getDataFromSensor()>0 and self.m.getDataFromSensor()<100

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()