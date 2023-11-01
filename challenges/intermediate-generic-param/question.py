"""
TODO:

Define a wrapper type with generic parameter.
"""


class Box:
    def __init__(self, value):
        self.value = value

    def unwrap(self):
        # This should return the wrapped type
        return self.value


def should_pass(w: Box[str]):
    a: str = w.unwrap()
    b: int = Box(1).unwrap()


def should_fail(w: Box[str]):
    a: int = w.unwrap()
    b: str = Box(1).unwrap()
