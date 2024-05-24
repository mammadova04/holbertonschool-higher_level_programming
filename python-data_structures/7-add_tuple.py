#!/usr/bin/python3
def check(tuple_c=()):
    if tuple_c == ():
        return (0, 0)
    elif len(tuple_c) == 1:
        return (tuple_c[0], 0)
    else:
        return tuple_c

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check(tuple_a)
    tuple_b = check(tuple_b)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
