#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number %= -10
        number *= -1
        print("{}".format(number), end="")
        return number
    else:
        number %= 10
        print("{}".format(number), end="")
        return number
