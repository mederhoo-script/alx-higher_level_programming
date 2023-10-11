#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tua = tuple_a + (0, 0)
    tub = tuple_b + (0, 0)
    new_tuple = tua[0] + tub[0], tua[1] + tub[1]
    return new_tuple
