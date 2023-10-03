#!/usr/bin/python3
def uppercase(str):
    c = ""
    for i in str:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        c += i
    print("{}".format(c), end="")
    print("{}".format(""))
