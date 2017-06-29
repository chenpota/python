from typing import List
#######################################


def func1() -> None:
    v = []  # error
    # do something
    v = [2]
#######################################


def func2() -> None:
    v = []  # type: ignore
    # do something
    v = [2]
#######################################


def func3() -> None:
    v = []  # type: List[int]
    # do something
    v = [2]
