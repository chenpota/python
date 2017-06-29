from typing import Iterator
#######################################


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fib(5)))
