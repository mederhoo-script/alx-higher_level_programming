#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if(number < 0):
    last = last % -10
else:
    last = last % 10
if(last
