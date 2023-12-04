def foo(x: list[str]):
    pass


## End of your code ##
foo(["foo", "bar"])
foo(["foo", 1])  # expect-type-error
