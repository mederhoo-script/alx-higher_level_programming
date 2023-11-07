#!/usr/bin/pythone3

def read_file(filename=""):
    with open(filename, "r", encoding='utf-8') as file:
        output = file.read()
        return output
