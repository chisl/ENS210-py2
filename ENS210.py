#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""ENS210: The ENS210 integrates one relative humidity sensor and one high-accuracy temperature sensor."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["AMS"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

from ENS210_constants import *

# name:        ENS210
# description: The ENS210 integrates one relative humidity sensor and one high-accuracy temperature sensor.
# manuf:       AMS
# version:     0.1
# url:         http://ams.com/eng/content/download/950231/2267959/483138
# date:        2017-09-03


# Derive from this class and implement read and write
class ENS210_Base:
	"""The ENS210 integrates one relative humidity sensor and one high-accuracy temperature sensor."""
	# Register PART_ID
	# Identifies the part as ENS210 
	
	def setPART_ID(self, val):
		"""Set register PART_ID"""
		self.write(REG.PART_ID, val, 16)
	
	def getPART_ID(self):
		"""Get register PART_ID"""
		return self.read(REG.PART_ID, 16)
	
	# Bits PART_ID
	# Register UID
	# This 8 byte register uniquely identifies a single device among all ENS210 devices. 
	
	def setUID(self, val):
		"""Set register UID"""
		self.write(REG.UID, val, 64)
	
	def getUID(self):
		"""Get register UID"""
		return self.read(REG.UID, 64)
	
	# Bits UID
	# Register SYS_CTRL
	# System configuration 
	
	def setSYS_CTRL(self, val):
		"""Set register SYS_CTRL"""
		self.write(REG.SYS_CTRL, val, 8)
	
	def getSYS_CTRL(self):
		"""Get register SYS_CTRL"""
		return self.read(REG.SYS_CTRL, 8)
	
	# Bits RESET
	# Write 1 to reset the device 
	# Bits reserved_0
	# Bits LOW_POWER
	# Controls the automatic low power. 
	# Register SYS_STAT
	# System status 
	
	def setSYS_STAT(self, val):
		"""Set register SYS_STAT"""
		self.write(REG.SYS_STAT, val, 8)
	
	def getSYS_STAT(self):
		"""Get register SYS_STAT"""
		return self.read(REG.SYS_STAT, 8)
	
	# Bits reserved_0
	# Bits SYS_ACTIVE
	# The system power state 
	# Register SENS_RUN
	# The run mode (single shot or continuous) 
	
	def setSENS_RUN(self, val):
		"""Set register SENS_RUN"""
		self.write(REG.SENS_RUN, val, 8)
	
	def getSENS_RUN(self):
		"""Get register SENS_RUN"""
		return self.read(REG.SENS_RUN, 8)
	
	# Bits reserved_0
	# Bits H_RUN
	# The run mode of the relative humidity sensor 
	# Bits T_RUN
	# The run mode of the temperature sensor 
	# Register SENS_START
	# Start measurement 
	
	def setSENS_START(self, val):
		"""Set register SENS_START"""
		self.write(REG.SENS_START, val, 8)
	
	def getSENS_START(self):
		"""Get register SENS_START"""
		return self.read(REG.SENS_START, 8)
	
	# Bits reserved_0
	# Bits H_START
	# Write a 1 to start a relative humidity sensor measurement. 
	# Bits T_START
	# Write a 1 to start a temperature sensor measurement. 
	# Register SENS_STOP
	# Stop continuous measurement 
	
	def setSENS_STOP(self, val):
		"""Set register SENS_STOP"""
		self.write(REG.SENS_STOP, val, 8)
	
	def getSENS_STOP(self):
		"""Get register SENS_STOP"""
		return self.read(REG.SENS_STOP, 8)
	
	# Bits reserved_0
	# Bits H_STOP
	# Write a 1 to stop a continuous relative humidity sensor measurement. 
	# Bits T_STOP
	# Write a 1 to stop a continuous temperature sensor measurement. 
	# Register SENS_STAT
	# Sensor status (idle or measuring) 
	
	def setSENS_STAT(self, val):
		"""Set register SENS_STAT"""
		self.write(REG.SENS_STAT, val, 8)
	
	def getSENS_STAT(self):
		"""Get register SENS_STAT"""
		return self.read(REG.SENS_STAT, 8)
	
	# Bits reserved_0
	# Bits H_STAT
	# Indicates the measuring status of the relative humidity sensor
	#           Write a 1 to stop a continuous relative humidity sensor measurement. 
	
	# Bits T_STAT
	# The run mode of the temperature sensor.
	#           Write a 1 to stop a continuous temperature sensor measurement. 
	
	# Register T_VAL
	# This 3 byte register contains the last measured temperature data. Furthermore it has a
	#       data valid flag and a CRC over the former two. Note that these bytes are double buffered;
	#       they are latched in by accessing the first byte, see The Sensor Readout Registers for
	#       details. 
	
	
	def setT_VAL(self, val):
		"""Set register T_VAL"""
		self.write(REG.T_VAL, val, 24)
	
	def getT_VAL(self):
		"""Get register T_VAL"""
		return self.read(REG.T_VAL, 24)
	
	# Bits T_CRC
	# CRC over T_DATA and T_VALID §
	# Bits T_VALID
	# Data valid indication (1 means T_DATA is valid) §
	# Bits T_DATA
	# Last measured temperature, stored as a little endian 16 bits unsigned value in 1/64 Kelvin §
	# Register H_VAL
	# This 3 byte register contains the last measured relative humidity data. Furthermore it
	#      has a data valid flag and a CRC over the former two. Note that these bytes are double
	#      buffered; they are latched in by accessing the first byte, see The Sensor Readout Registers
	#      for details. 
	
	
	def setH_VAL(self, val):
		"""Set register H_VAL"""
		self.write(REG.H_VAL, val, 24)
	
	def getH_VAL(self):
		"""Get register H_VAL"""
		return self.read(REG.H_VAL, 24)
	
	# Bits H_CRC
	# CRC over H_DATA and H_VALID
	# Bits H_VALID
	# Data valid indication (1 means H_DATA is valid)
	# Bits H_DATA
	# Last measured relative humidity, stored as a little endian 16 bits unsigned value in 1/512%RH
