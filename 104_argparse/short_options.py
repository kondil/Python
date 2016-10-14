#!/usr/bin/env python3

# This is a tutorial based on 
# https://docs.python.org/3.5/howto/argparse.html

# Introducing Optional Arguments

import argparse

parser = argparse.ArgumentParser ()

parser.add_argument("-v", "--verbose", help="increase output verbosity", action="count")

args = parser.parse_args()

if args.verbose:
    print("verbosity turned on")
    print(args)

