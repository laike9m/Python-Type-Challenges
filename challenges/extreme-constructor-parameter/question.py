"""
TODO:

Define a decorator `constructor_parameter` that accepts the type of Foo.
and return a wrapper function with the same signature as the constructor of Foo,
and function decorated by `constructor_parameter` can be called with an instance of Foo.
"""

def constructor_parameter():
    ...


## End of your code ##
class Foo:
    a: int
    b: str

    def __init__(self, a: int, b: str) -> None:
        ...


@constructor_parameter(Foo)
def func_pass(foo: Foo) -> list[Foo]:
    ...


res = func_pass(1, "2")
res[0].a.bit_length()
res[0].b.upper()


@constructor_parameter(Foo)
def func_fail(foo: Foo) -> list:
    ...


func_fail("1", "2")  # expect-type-error
func_fail([1, 2, 3])  # expect-type-error
