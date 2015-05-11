#!/usr/bin/env python

# Temporary python script about datetime.

import datetime

def us2eudtf(inputDT):
	return datetime.datetime(inputDT.year, inputDT.day, inputDT.month)

print us2eudtf(datetime.datetime(2015, 8, 4, 0, 0))


