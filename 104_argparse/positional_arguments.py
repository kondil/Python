#!/usr/bin/env python3

# This is a tutorial based on 
# https://docs.python.org/3.5/howto/argparse.html

# Introducing Positional Arguments

import argparse

parser = argparse.ArgumentParser ()

# Add an argument of type str
parser.add_argument("echo", help="this is the help for the echo option")

# The argparse treats all options as strings by default
# We should explicitly tell it otherwise if needed
# Add an argument of type int
parser.add_argument("square", help="display a square of a given number", type=int)


args = parser.parse_args()
print(args.echo)
print(args.square**2)
