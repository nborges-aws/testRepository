from typing import Iterable

def add(*args: int) -> int:
    return sum(args)

def add_stream(numbers: Iterable[int]) -> int:
    return sum(numbers)