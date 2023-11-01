"""
TODO:
    Define a protocol for class `SupportsQuack` that supports a "quack" method.
"""

from typing import Protocol


class SupportsQuack:
    ...


class Duck:
    def quack(self) -> None:
        print("quack!")


class Dog:
    def bark(self) -> None:
        print("bark!")


def should_pass():
    duck: SupportsQuack = Duck()


def should_fail():
    dog: SupportsQuack = Dog()
