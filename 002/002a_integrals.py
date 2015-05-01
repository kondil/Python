#!/usr/bin/env python

# The following is a bool type that is considered as integral in Python.
boolX = True 	# This should be treated as 1 but I haven't tested it yet.
print boolX

boolX = False	# This should be treated as 0 but I haven't tested it yet.
print boolX

# Integers

ip = 5
print ip

# Longs

lq = 7L
ip = ip ** 35
print ip, lq

# Hexadecimals

hp = 0x3F

print hp	# This will actually print 63 wich is the decimal version of 0x3F.

