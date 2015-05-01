#!/usr/bin/env python

# Python provides three kinds of floating-point values: 

# - float 	:: Double Precision floating point.
#   - Their range depends on the C or Java compiler Python was built with.
#   - They have limited precision and cannot be reliably compared for equality.

f1 = 19
f2 = 5.1				# In principal .1 is not properly represented.

print f1, f2

# - Decimal 	:: Higher Precision floating point.
#   - They perform calculations that are accurate to the level of precision we specify.
#   - Processing them is a lot slower than with normal floats.
#   - To use them we need to import decimal.

import decimal

dec1 = decimal.Decimal(19)
dec2 = decimal.Decimal("5.1")
dec3 = decimal.Decimal("8.9e-4")

print dec1,dec2,dec3

# - complex

c1 = 5.4 + 0.8j
print c1, type(c1)

