#!/usr/bin/python3
from sys import argv


def args_print():
    j = len(argv) - 1
    print("{} arguments:".format(j))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[1]))
        j += 1


if __name__ == "__main__":
    args_print()
