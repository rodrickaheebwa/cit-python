# 1. Import argparse
# 2. Create a parser -> argparse.ArgumentParser(), and add a description
# 3. Add arguments to the created parser -> parser.add_argument()
# 4. Parse the arguments -> parser.parse_args()
# The variable args = parser.parse_args() will contain the values stored in those arguments and can be accessed using the dot notation -> args.argument
# E.g. calc_area.py length width -> run like: calc_area.py 4 2 >> 8
# By default, the arguments created are positional, which don't require a flag to be accessed, but the order has to be followed
# To create positional arguments, use flags, both short and long notations
# E.g. calc_area.py [-l --length] [-H --height] -> run like: calc_area.py -l 4 -H 2 >> 8
# Because they are always optional, always use the required=True parameter where needed

# Passing in a value without the command name is only accepatable for positional arguments, the moment you use flags, you have to supply both tag and value

import argparse

parser = argparse.ArgumentParser()

parser.add_argument()

args = parser.parse_args()