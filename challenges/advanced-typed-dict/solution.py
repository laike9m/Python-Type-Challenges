"""
TODO:

Define a class `Point3D` using the predefined Point2D.
`Point3D` needs to have an extra key-value pair: z - int
"""

from typing import TypedDict


class Point2D(TypedDict):
    x: int
    y: int
    label: str


class Point3D(Point2D):
    z: int


## End of your code ##
a: Point3D = {"x": 1, "y": 2, "z": 3, "label": "good"}
a: Point3D = {"x": 1, "z": 2, "label": "good"}  # expect-type-error
a: Point3D = {"x": 1, "y": 2, "label": "good"}  # expect-type-error
assert Point3D(x=1, y=2, z=3, label="first") == dict(x=1, y=2, z=3, label="first")
