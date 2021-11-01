from typing import Any, TypeVar

T = TypeVar("T", int, float, str)


def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    pass


def divide(a: int, b: int) -> int:
    pass


def power(a: int, b: int) -> int: 
    pass


def combine(a: str, b: str) -> str:
    return a + b


def add_float(a: float, b: float) -> float:
    return a + b


def no_type_add(a: T, b: T) -> T:
    return a + b