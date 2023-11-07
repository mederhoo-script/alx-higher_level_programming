#!/usr/bin/python3
"""define a function that writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """function that write a string to utf8 file

        Args:
            filename: name of the file.
            w:
            open with write permision

        Rrturn: writed str
    """
    with open(filename, "w", encoding='utf_8') as file:
        file.write(text)
