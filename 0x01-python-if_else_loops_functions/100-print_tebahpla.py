#!/usr/bin/python3
j = 25
for i in range(ord('a'), ord('z') + 1):
    i = i + j
    if (i + 1) % 2 == 0:
        i -= 32
    i = chr(i)
    print("{}".format(i), end="")
    j -= 2
