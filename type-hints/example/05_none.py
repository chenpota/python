from typing import NamedTuple, Optional, Union


Person = NamedTuple(
    'Person',
    [
        ('name', str),
        ('age', int),
    ])


def pass_person(v: Person):
    pass

pass_person(Person('Alex', 30))
pass_person(Person('Alex', None))  # type error if mypy --strict-optional

PersonV2 = NamedTuple(
    'PersonV2',
    [
        ('name', str),
        ('age', Optional[int]),  # perfered format
    ])


def pass_person_v2(v: PersonV2):
    pass

pass_person_v2(PersonV2('Alex', 30))
pass_person_v2(PersonV2('Alex', None))

PersonV3 = NamedTuple(
    'PersonV3',
    [
        ('name', str),
        ('age', Union[int, None]),
    ])


def pass_person_v3(v: PersonV3):
    pass

pass_person_v3(PersonV3('Alex', 30))
pass_person_v3(PersonV3('Alex', None))
