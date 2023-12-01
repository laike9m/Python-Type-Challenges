"""
TODO:

Define a class `Student` that represents a dictionary with three keys:
- name, a string
- age, an integer
- school, a string
"""


## End of your code ##
a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
a: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  # expect-type-error
a: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  # expect-type-error
a: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"}  # expect-type-error
a: Student = {"name": "Tom", "age": 2}  # expect-type-error
assert Student(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)
