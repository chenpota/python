from typing import List, Union, cast
#######################################


def merge_list1(
        lhs: List[int],
        rhs: List[str]) -> List[Union[int, str]]:
    return lhs + rhs  # error

print(merge_list1([1, 2], ['a', 'b']))
#######################################


def merge_list2(
        lhs: List[int],
        rhs: List[str]) -> List[Union[int, str]]:
    return lhs + rhs  # type: ignore

print(merge_list2([1, 2], ['a', 'b']))
#######################################


def merge_list3(
        lhs: List[int],
        rhs: List[str]) -> List[Union[int, str]]:
    cast_lhs = cast(List[Union[int, str]], lhs)
    cast_rhs = cast(List[Union[int, str]], rhs)
    return cast_lhs + cast_rhs

print(merge_list3([1, 2], ['a', 'b']))
