"""
TODO:

`a` should be an integer.
"""


a


def should_pass():
    global a
    a = 2


def should_fail():
    global a
    a = "1"
