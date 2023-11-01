"""
TODO:

Define a function that accepts two parameters of the same type and returns the same type.
The type can only be str or int.
"""


from typing import List


def add(a, b):
    return a


def should_pass():
    c: int = add(1, 2)
    d: str = add("1", "2")


def should_fail():
    e: List[str] = add(["1"], ["2"])
