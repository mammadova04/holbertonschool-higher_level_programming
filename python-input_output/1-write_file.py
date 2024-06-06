#!/usr/bin/python3
"""C-deki read write syscall'lara qurban olaram"""


def write_file(filename="", text=""):
    """writing to a file"""
    with open(filename, 'w', encoding="utf-8") as fd:
        return fd.write(text)
