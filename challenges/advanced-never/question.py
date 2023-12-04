"""
TODO:

Make sure `never_call_me` is never called.
"""


def never_call_me(arg):
    pass


## End of your code ##
def int_or_str(arg: int | str) -> None:
    never_call_me(arg)  # expect-type-error
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _:
            never_call_me(arg)
