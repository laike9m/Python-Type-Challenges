"""
TODO:

a method-like descriptor, implements the `__get__` only.
"""
from typing import Any, ParamSpec, TypeVar, Concatenate, Callable, Generic, overload

P = ParamSpec("P")
T = TypeVar("T")
R = TypeVar("R")

class MyMethod(Generic[T, P, R]):
    def __init__(self, func: Callable[Concatenate[T, P], R]) -> None:
        self.func = func
    
    @overload
    def __get__(self, instance: None, owner: type) -> Callable[Concatenate[T, P], R]:
        ...
    
    @overload
    def __get__(self, instance: Any, owner: type) -> Callable[P, R]:
        ...
    
    def __get__(self, instance: Any | None, owner: type):
        if instance is None:
            return self.func

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            return self.func(instance, *args, **kwargs)
    
        return wrapper


## End of your code ##
class Foo:
    @MyMethod
    def do_something(self, value: int) -> None:
        ...

foo = Foo()

Foo.do_something(foo, 1111)
foo.do_something(1111)


Foo.do_something(1111)  # expect-type-error
foo.do_something(11111, foo)  # expect-type-error
foo.do_something(foo, 11111)  # expect-type-error
