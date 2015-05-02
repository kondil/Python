#!/usr/bin/env python

# Tuples
# - They are immutable, so we cannot replace or delete any of their items.

empty = ()
print "empty = ", empty, ", type of empty = ", type(empty)

one = ("Canary")
print "one = ", one, ", type of one = ", type(one)

one = ("Canary", )
print "one = ", one, ", type of one = ", type(one)

things = ("Parrot", 3.5, u"\u20AC")
print "things = ", things, " type of things = ", type(things)

items = "Parrot", 28, 'Cow', 32.5
print "items = ", items, " type of items = ", type(items)
print "items[:2] = ", items[:2], " items[3] = ", items[3]

# - The slices of the tuples are always slices themselves.

items = items[:2], 'newEntry', items[2:]
print "Items = ", items
print "A different type of slice :: items[0:3:2] = ", items[0:3:2]
print "A way of chopping the last item is :: items[:-1] = ", items[:-1]
print "Length of the tuple is ", len(items)
print "items[0][1] = ", items[0][1]
print "items[2][0] = ", items[2][0]
print "tuple('some text') = ", tuple("some text")
