"""
TODO:

`make_object` takes a class returns an instance of it.
"""


def make_object(cls):
    return cls()


## End of your code ##
class MyClass:
    pass


def f():
    pass


c = make_object(MyClass)
c = make_object(int)
c = make_object(f)  # expect-type-error
c = make_object("sss")  # expect-type-error
c = make_object(["sss"])  # expect-type-error
