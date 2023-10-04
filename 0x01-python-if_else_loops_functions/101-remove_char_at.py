#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    if n >= len(str):
        return str
    c = ""
    n = int(n)
    for i in str:
        if i == str[n]:
            i = ""
        c += i
    return c
