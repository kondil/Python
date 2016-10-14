#!/usr/bin/env python3

# This is a tutorial based on 
# https://docs.python.org/3.5/howto/argparse.html

# Introducing Optional Arguments

import argparse

parser = argparse.ArgumentParser ()

# In order to set optional arguments we should use the "--"
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()

if args.verbosity:
    print("verbosity turned on")

