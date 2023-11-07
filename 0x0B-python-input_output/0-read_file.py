#!/usr/bin/pythone3
"""a function that reads a text file (UTF8) and prints it to stdout:"""

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
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
    """
    with open(filename, "r", encoding='utf-8') as file:
        output = file.read()
        print(output, end="")
