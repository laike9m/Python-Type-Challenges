"""
TODO:

Define a decorator `constructor_parameter` that input target class 
and return a wrapper function with the same signature as the constructor of the target class, 
and function which decorated by `constructor_parameter` can be called with the instance of the target class.
"""

class Foo:
    def __init__(self, a: int, b: str) -> None:
        ...

def constructor_parameter():
    ...


def should_pass():
    @constructor_parameter(Foo)
    def func(foo: Foo) -> list:
        ...

    res = func(1, "2")
    res.append(1)


def should_fail():
    @constructor_parameter(Foo)
    def func(foo: Foo) -> list:
        ...

    func("1", "2")
    func([1, 2, 3])
