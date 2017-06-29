from typing import Callable, get_type_hints
#######################################


def function1(v: int) -> None:
    pass


def function2(v: str) -> None:
    pass


def caller(cb: Callable[[int], None]) -> None:
    cb(1)

caller(function1)
caller(function2)  # error
#######################################


# PEP 484 not support lambda
lambda_func1 = lambda v: int(v)
lambda_func2 = lambda v: v + 1

caller(lambda_func1)  # error
caller(lambda_func2)  # error?
