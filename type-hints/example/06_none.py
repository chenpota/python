from typing import Optional, Union
#######################################


def func_pass_int(v: int) -> None:
    pass


def func_pass_int_or_none_v1(v: Optional[int]) -> None:  # perfered format
    pass


def func_pass_int_or_none_v2(v: Union[int, None]) -> None:
    pass

func_pass_int(None)  # error if mypy --strict-optional
func_pass_int_or_none_v1(None)
func_pass_int_or_none_v2(None)
#######################################


def func_with_default_args_v1(v: int = None) -> None:  # perfered format
    pass

func_with_default_args_v1()
func_with_default_args_v1(None)  # no error if mypy --strict-optional


def func_with_default_args_v2(v: Optional[int] = None) -> None:
    pass

func_with_default_args_v2()
func_with_default_args_v2(None)
#######################################


def func_return_int() -> int:
    return None  # error if mypy --strict-optional


def func_return_int_or_none_v1() -> Optional[int]:  # perfered format
    return None


def func_return_int_or_none_v2() -> Union[int, None]:
    return None
