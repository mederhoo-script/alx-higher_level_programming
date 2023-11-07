#!/usr/bin/pythone3

def read_file(filename=""):
    with open(filename, "r") as file:
        output = file.read()
        return output
