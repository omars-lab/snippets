#!/usr/bin/python
from timeit import Timer


def lets_timeit():
    """
    The timeit Time lets us time how long it takes to evaluate python
    expressions
    """
    Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
    Timer('a,b = b,a', 'a=1; b=2').timeit()

lets_timeit()
