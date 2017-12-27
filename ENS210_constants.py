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

class REG:
	PART_ID = 0
	UID = 4
	SYS_CTRL = 16
	SYS_STAT = 17
	SENS_RUN = 33
	SENS_START = 34
	SENS_STOP = 35
	SENS_STAT = 36
	T_VAL = 48
	H_VAL = 51
