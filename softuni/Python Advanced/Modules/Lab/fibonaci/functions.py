def create(num):
    return [fibonacci_of(n) for n in range(num)]


def locate(num, fibo):
    if num in fibo:
        return f"The number - {num} is at index {fibo.index(num)}"
    else:
        return f'The number {num} is not in the sequence'


def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)
