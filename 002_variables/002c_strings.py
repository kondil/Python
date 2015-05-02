#!/usr/bin/env python

# There are two built-in string types in Python: 
# - str 	:: Bytes

str1 = "Green"
str2 = 'Red'

print str1, str2, str1 + str2
print type(str1), type(str2)

#   - They are sequences.

phrase = "This is a phrase."
print "phrase = ", phrase			# Let's print the phrase.
print phrase[1], phrase[10], phrase[13]		# Or some parts of the sequence.
print phrase[-1], phrase[-3] 			# Or backwards.
print phrase[:4]				# Or some subsequences.
print phrase[:-3]
print phrase[-7:-3] 
print "Parts with specific step :: ", phrase[1:5:2]
print "Let's find some subsequence :: phrase.find('s') = ", phrase.find("s")
print "Let's find some subsequence :: phrase.find('is') = ", phrase.find("is")
print "Let's find some subsequence :: phrase.find(' is') = ", phrase.find(" is")
print "Let's find some subsequence :: phrase.find('no') = ", phrase.find("no")
print "'no' in phrase :: ", "no" in phrase
print "'This' in phrase :: ", "This" in phrase

#   - They are immutable. This means that we cannot change specific part of the string value without changing the whole string.
p = "pad"
# p[1] = "o" # This will fail but what we can do is ::
p = p[:1] + 'o' + p[2:]
print p


# - unicode 	:: Unicode characters. 
str3 = u"Green"

print str2, str3, str2+str3
print type(str2), type(str3), type(str2+str3)

# Test Stuff
euro = unichr(8364)
print euro, ord(euro)

euro = u"\N{euro sign}"
print euro

