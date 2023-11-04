"""
TODO:

Define a `Tree` type. `Tree` is a dictionary, whose keys are string, values are also `Tree`.
"""

Tree = ...


## End of your code ##
def f(t: Tree):
    pass


f({})
f({"foo": {}})
f({"foo": {"bar": {}}})
f({"foo": {"bar": {"baz": {}}}})


f(1)  # expect-type-error
f({"foo": []})  # expect-type-error
f({"foo": {1: {}}})  # expect-type-error
