"""
TODO:

Define a class `Point2D` that represents a dictionary with three string keys:
    x, y, label

The value of each key must be the specified type:
    x - int, y - int, label - str

Note: label is optional
"""


## End of your code ##
a: Point2D = {"x": 1, "y": 2}
a: Point2D = {"x": 1, "y": 2, "label": "good"}
a: Point2D = {"x": 1, "z": 2, "label": "good"}  # expect-type-error
a: Point2D = {(1,): 1, "y": 2, "label": "good"}  # expect-type-error
a: Point2D = {"x": 1, "y": "2", "label": "good"}  # expect-type-error
b: Point2D = {"z": 3, "label": "bad"}  # expect-type-error
assert Point2D(x=1, y=2) == dict(x=1, y=2)
assert Point2D(x=1, y=2, label="first") == dict(x=1, y=2, label="first")
