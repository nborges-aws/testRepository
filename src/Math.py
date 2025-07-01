def add(a: int, b: int) -> int:
    return a + b

def fibonacci(idx: int):
    if idx <= 1:
        return idx
    
    return fibonacci(idx - 1) + fibonacci(idx - 2)