#!/usr/bin/python3
def uniq_add(my_list=[]):
    y = []
    for i in my_list:
        if i not in y:
            y.append(i)
    return sum(y)
