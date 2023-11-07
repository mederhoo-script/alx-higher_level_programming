#!/usr/bin/pythone3
"""define a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """
Read the content of a file and return it as a string.

Args:
    filrname: the name the file to read.

    Return:
        str: the file content as string

    Raises:
        nothing yet.

    E.g:
        >>> read_file("tests/my_file_0.txt")
        We offer a truly innovative approach to education:
focus on building reliable applications and scalable s
    """
    with open(filename, encoding='utf-8') as file:
        output = file.read()
        print(output, end="")
