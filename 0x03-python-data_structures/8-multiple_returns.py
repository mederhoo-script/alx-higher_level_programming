#!/usr/bin/python3
def multiple_returns(sentence):
    i = ()
    if len(sentence) == 0:
        i = 0, "None"
    else:
        i = len(sentence), sentence[0]
    return i
