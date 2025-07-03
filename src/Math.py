def add(a: int, b: int) -> int:
    return a + b

def multiply(*args: int) -> int:
    result = 1
    for num in args:
        result *= num
    return result