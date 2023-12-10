"""
TODO:

Define a class `Question` with optional key `tags`
"""


from typing import List, TypedDict


class Question(TypedDict):
    title: str
    content: str
    tags: List[str]


## End of your code ##
a: Question = {"title": "foo", "content": "bar"}
