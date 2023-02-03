#!/usr/bin/python3


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    xs = range(0, n + 1)
    xs = filter(lambda x: x % 2 == 0, xs)
    xs = list(xs)
    return xs
