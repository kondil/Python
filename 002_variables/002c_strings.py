#!/usr/bin/env python

# There are two built-in string types in Python: 
# - str 	:: Bytes
#   - They are immutable.
#   - They are also sequences.

str1 = "Green"
str2 = 'Red'
str3 = u"Green"

print str1, str2, str1 + str2, str2+str3
print type(str1), type(str2), type(str3), type(str2+str3)

# - unicode 	:: Unicode characters. 



