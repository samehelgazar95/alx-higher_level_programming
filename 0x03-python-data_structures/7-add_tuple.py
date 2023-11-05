#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    ta2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    tb1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    tb2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    return (ta1 + tb1, ta2 + tb2)
