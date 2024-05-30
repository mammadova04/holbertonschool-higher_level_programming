#!/usr/bin/python3
"""prints text"""


def text_indentation(text):
    """func"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in ".:?":
        text = text.replace(c, c + "\n\n")
    print("\n".join(s.strip() for s in text.split("\n")), end="")
