"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string

Note: school can be optional
"""

from typing import TypedDict, NotRequired


class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]


# Alternatively you can write:
# Student = TypedDict('Student', {'name': str, 'age': int, 'school': str})


## End of your code ##
a: Student = {"name": "Tom", "age": 15}
a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
a: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  # expect-type-error
a: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  # expect-type-error
a: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"}  # expect-type-error
a: Student = {"z": "Tom", "age": 2}  # expect-type-error
assert Student(name="Tom", age=15) == dict(name="Tom", age=15)
assert Student(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)
