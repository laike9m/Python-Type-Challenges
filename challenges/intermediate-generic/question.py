"""
TODO:

Define a function that accepts two parameters of the same type and returns the same type.
"""


from typing import List


def add(a, b):
    return a


def should_pass():
    c: int = add(1, 2)
    d: str = add("1", "2")
    e: List[str] = add(["1"], ["2"])


def should_fail():
    c: int = add(1.0, 2.2)
    d: int = add("1", "2")
