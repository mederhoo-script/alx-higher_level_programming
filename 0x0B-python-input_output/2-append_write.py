#!/usr/bin/python3
"""define a function that writes a string to a text file (UTF8) """


def append_write(filename="", text=""):
    """function that append a string to utf8 file

        Args:
            filename: name of the file.
            text: sting to be apennd
            a: open with append permision

        Rrturn: writed str
    """
    with open(filename, "a", encoding='utf_8') as file:
        return file.write(text)
