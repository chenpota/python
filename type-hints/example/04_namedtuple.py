from collections import namedtuple
from typing import NamedTuple

Person = namedtuple(
    'Person',
    (
        'name',  # str
        'age'   # int
    ))


def func1(v: Person) -> None:
    pass

func1(Person('Alex', 30))
func1(Person('Alex', '30'))  # type error, but any analyzer can't detect it.

TypeHintsPerson = NamedTuple(
    'TypeHintsPerson',
    [
        ('name', str),
        ('age', int),
    ])


def func2(v: TypeHintsPerson) -> None:
    pass

func2(TypeHintsPerson('Alex', 30))
func2(TypeHintsPerson('Alex', '30'))  # type error
