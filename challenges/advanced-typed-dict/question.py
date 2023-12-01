"""
TODO:

Define a class `Undergraduate` using the predefined class `Student`.
`Undergraduate` has an extra key `major` of type string
"""

from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: str


class Undergraduate:
    ...


## End of your code ##
a: Undergraduate = {"name": "Tom", "age": 20, "school": "MIT", "major": "Math"}
a: Undergraduate = {"name": "Tom", "age": 20, "school": "MIT"}  # expect-type-error
assert Undergraduate(name="Tom", age=20, school="MIT", major="Math") == {
    "name": "Tom",
    "age": 20,
    "school": "MIT",
    "major": "Math",
}
