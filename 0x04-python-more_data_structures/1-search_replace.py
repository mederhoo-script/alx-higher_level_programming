#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list[:]
    x = []
    for i in nlist:
        if i == search:
            i = replace
        x.append(i)
    return x