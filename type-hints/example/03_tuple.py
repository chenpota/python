from typing import Any, Tuple
#######################################


def pass_builtin_tuple_v1(v: tuple) -> None:
    pass

pass_builtin_tuple_v1(())
pass_builtin_tuple_v1((1, 's'))


def pass_builtin_tuple_v2(v: Tuple[Any, ...]) -> None:
    pass

pass_builtin_tuple_v2(())
pass_builtin_tuple_v2((1, 's'))
#######################################


def pass_tuple_with_str(v: Tuple[str]) -> None:
    pass

pass_tuple_with_str(())  # error
pass_tuple_with_str(('text',))
pass_tuple_with_str(('text', 1))  # error
#######################################


def pass_empty_tuple(v: Tuple[()]) -> None:
    pass

pass_empty_tuple(())
pass_empty_tuple(('text',))  # error
pass_empty_tuple(('text', 1))  # error
#######################################


def pass_tuple_with_str_int(v: Tuple[str, int]) -> None:
    pass

pass_tuple_with_str_int(())  # error
pass_tuple_with_str_int(('text',))  # error
pass_tuple_with_str_int(('text', 1))
