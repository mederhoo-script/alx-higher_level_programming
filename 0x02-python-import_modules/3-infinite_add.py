#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    agc = len(argv) - 1
    total = 0
    for i in range(1, len(argv)):
        total += int(argv[i])
    print(total)
