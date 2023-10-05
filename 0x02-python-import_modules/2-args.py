#!/usr/bin/python3
if __name__ == "__main__":
    import sys


    def args_print():
        j = len(sys.argv) - 1
        if j == 0:
            print("{} argument:".format(j))
        else:
            print("{} arguments:".format(j))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[1]))
            j += 1


args_print()
