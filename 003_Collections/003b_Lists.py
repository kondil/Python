#!/usr/bin/env python

# List is an ordered sequence type similar to the tuple type.
# - All the sequence functions and the slicing work in exactly the same way for lists.
# - They are mutables and there methods to modify the lists.
# - They are created using square brackets.

print '>> fruit = ["Apple", "Hawthorn", "Loquat", "Medlar", "Pear", "Quince"]'
fruit = ["Apple", "Hawthorn", "Loquat", "Medlar", "Pear", "Quince"]
print "fruit = ", fruit
print "fruit[:2] = ", fruit[:2]
print "fruit[-1] = ", fruit[-1]

fruit.insert(4, "Rowan")
print fruit

del fruit[4]
print fruit

# - Or we can do the same using slicing.
fruit[4:4] = ["Rowan"]
print "Added a fruit using slicing. ", fruit

print '>> fruit[4:5] = []'
fruit[4:5] = []
print "Deleted the fruit using slicing. ", fruit

# Append in the end of the list.
print '>> fruit.append("Watermelon")'
fruit.append("Watermelon")
print fruit

print '>> fruit.insert(7,"NooN")'
fruit.insert(7,"NooN")
print fruit

print '>> fruit.insert(7,"NaaN")'
fruit.insert(7,"NaaN")
print fruit

print '>> print len(fruit)'
print len(fruit)

