"""
TODO:

Define a `Tree` type. `Tree` is a dictionary, whose keys are string, values are also `Tree`.
"""
from typing import Dict, TypeAlias

# For Python < 3.12
# Tree : TypeAlias = Dict[str, 'Tree']

type Tree = Dict[str, 'Tree']


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
