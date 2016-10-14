#!/usr/bin/env python3

# This is a tutorial based on 
# https://docs.python.org/3.5/howto/argparse.html

# Introducing Optional Arguments

import argparse

parser = argparse.ArgumentParser ()

parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

args = parser.parse_args()
answer = args.square**2

args = parser.parse_args()

if args.verbose:
    print("the square of {} equals {}".format(args.square, answer))
else:
    print(answer)
    print(args)

