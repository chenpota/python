from typing import Any, List, TypeVar, Union


def pass_bulitin_list_v1(v: list) -> None:
    pass

pass_bulitin_list_v1([])
pass_bulitin_list_v1([1, 's'])


def pass_bulitin_list_v2(v: List[Any]) -> None:
    pass

pass_bulitin_list_v2([])
pass_bulitin_list_v2([1, 's'])


def pass_list_with_int(v: List[int]) -> None:
    pass

pass_list_with_int([])
pass_list_with_int([1, 2])
pass_list_with_int([1, 'text'])  # type error


def pass_list_with_str_int(v: List[Union[str, int]]) -> None:
    pass

pass_list_with_str_int([])
pass_list_with_str_int([1, 2])
pass_list_with_str_int([1, 'text'])
pass_list_with_str_int([1, 'text', 3.4])  # type error
