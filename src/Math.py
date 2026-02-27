def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Cannot perform modulo by zero")
    return a % b


def power(a: int, b: int) -> int:
    return a ** b


def absolute(a: int) -> int:
    return abs(a)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_even(a: int) -> bool:
    return a % 2 == 0


def is_odd(a: int) -> bool:
    return a % 2 != 0


def max_of(a: int, b: int) -> int:
    return a if a >= b else b


def min_of(a: int, b: int) -> int:
    return a if a <= b else b
