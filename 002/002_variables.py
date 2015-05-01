#!/usr/bin/env python

# Variables in python are actually object references and not actual objects themselves.
# Obect references are actually the address of the object in the memory space.
# Objects are the containers of the values we want to store.

# This is an integer variable
x = 71
print x
print id(x) 		# Prints the Address in the memory space.

x_ref = x		# This creates a copy of the object reference and not the object itself.
print x_ref
print id(x_ref)

x += 9			# This command will not only add the value of 9 in the object referenced by x but it will also create a new object.
print x, id(x)		# The x now refers to a new object.
print x_ref, id(x_ref)	# The x_ref references to the old x (before the addition).


# This is a float variable.
xf = .5
print xf

# This is a str variable
y = "Dove"
print y
print id(y) 		# Prints the Address in the memory space.

# Lets try to add 2 variables of different type.
print x + xf
print x + y



