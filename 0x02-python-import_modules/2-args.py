#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    j = len(sys.argv) - 1
    if j == 1:
        print("1 argument:")
    elif j == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(j))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
