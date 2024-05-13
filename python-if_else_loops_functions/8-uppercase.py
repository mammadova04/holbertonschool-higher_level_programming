#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            up_char = chr(ord(i) - 32)
            print("{}".format(up_char), end='')
        else:
            print("{}".format(i), end='')
