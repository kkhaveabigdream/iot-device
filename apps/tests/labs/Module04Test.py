"""
Test class for all requisite Module03 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""

import unittest
from labs.common.ConfigUtil import ConfigUtil
from labs.common.SensorData import SensorData
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.common.ActuatorData import ActuatorData
from labs.module03.SensorDataManager import SensorDataManager


class Module03Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.config = ConfigUtil()
		self.config.loadConfig('../../../config/ConnectedDevicesConfig.props')
		self.tempsensor = TempSensorAdaptorTask()
		self.sensordata = SensorData()
		self.actuatordata = ActuatorData()
		self.sensordata.addValue(10)
		self.sensordata.addValue(15)
		self.sensordata.addValue(20)
		self.sensordata.addValue(25)
		self.sensordata.setName('Temperature')
		self.actuatordata.setCommand('Increasing')
		self.actuatordata.setName('SenseHat')
		self.sdmanager = SensorDataManager()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		pass

	"""
	Place your comments describing the test here.
	"""
	
	def testloadConfig(self):	
		self.assertTrue(self.config.loadConfig('../../../config/ConnectedDevicesConfig.props') )
		
	def testhasConfigData(self):
		self.assertTrue(self.config.hasConfigData())
		
	def testgetValue(self):
		self.assertEqual(self.config.getValue("smtp.cloud","port"), '465')
		
	def testgetSensorData(self):
		assert self.tempsensor.getTemperature()>0 and self.tempsensor.getTemperature()<30
		
	def testgetAverageValue(self):
		assert self.sensordata.getAverageValue()>0 and self.sensordata.getAverageValue()<30
	
	def testgetCount(self):
		self.assertEqual(self.sensordata.getCount(),4)
		
	def testgetCurrentValue(self):
		assert self.sensordata.getCurrentValue()>0 and self.sensordata.getCurrentValue()<30
		
	def testMinValue(self):
		assert self.sensordata.getMinValue()>=0 and self.sensordata.getMinValue()<30
	
	def testMaxValue(self):
		assert self.sensordata.getMaxValue()>0 and self.sensordata.getMaxValue()<30
		
	def testName(self):
		self.assertEqual(self.sensordata.getName(), 'Temperature')
		
	def testgetCommand(self):
		self.assertEqual(self.actuatordata.getCommand(), 'Increasing')
	
	def testName2(self):
		self.assertEqual(self.actuatordata.getName(),'SenseHat')
	
	def testhandleSenseData(self):
		assert self.sdmanager.handleSensorData(self.sensordata) is not None
		
	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()