#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    def args_print():
        j = len(argv) - 1
        if j == 1:
            print("{} argument:".format(j))
        elif j == 0:
            print("{} arguments.".format(j))
        else:
            print("{} arguments:".format(j))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[1]))


args_print()
