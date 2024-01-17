"""
TODO:

Annotate class `MyContainer`, which should support item access, i.e.
using `[x]` to get, set, and delete an item.

HINT: Use https://github.com/python/typeshed/blob/main/stdlib/_typeshed/__init__.pyi
"""


class MyContainer:
    ...


## End of your code ##
from typing import assert_type
from collections.abc import Mapping

c = MyContainer()
c[1] = 1
c["2"] = 2
print(c[1])
print(c["2"])
del c[1]
del c["2"]
assert_type(c, dict)  # expect-type-error
assert_type(c, Mapping)  # expect-type-error
