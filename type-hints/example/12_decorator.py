import functools
from typing import TypeVar, cast
import decorator
#######################################


T = TypeVar('T')


def my_decorator(f: T) -> T:
    @functools.wraps(f)  # type: ignore
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)  # type: ignore

    return cast(T, wrapper)


@my_decorator
def func(v: int) -> None:
    pass

func(3)
func('3')  # error
