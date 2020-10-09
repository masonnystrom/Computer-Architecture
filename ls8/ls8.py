#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

# def main(argv):
#     """Main."""

#     if len(argv) != 2:
#         print(f"usage: {argv[0]} filename", file=sys.stderr)
#         return 1

#     cpu = CPU()
#     cpu.load(argv[1])
#     cpu.run()

#     return 0

# if __name__ == "__main__":
#     sys.exit(main(sys.argv))

import sys
from cpu2 import *


if len(sys.argv) != 2:
    raise TypeError('Enter a filename')
filename = sys.argv[1]

cpu = CPU(filename)

cpu.load()
cpu.run()

# # how to run day 1 mod
# cpu = CPU()
# cpu.load()
# cpu.run()