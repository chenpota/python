def pass_int(v: int) -> None:
    pass

pass_int(3.4)  # type error
pass_int(5)


def pass_float(v: float) -> None:
    pass

pass_float(3.4)
pass_float(5)


def pass_str(v: str) -> None:
    pass

pass_str('text')
pass_str(3.4)  # type error


def pass_bool(v: bool) -> None:
    pass

pass_bool(3 == 3)
pass_bool(3)  # type error


def pass_list(v: list) -> None:
    pass

pass_list([])
pass_list([1, 's'])
pass_list(())  # type error


def pass_tuple(v: tuple) -> None:
    pass

pass_tuple(())
pass_tuple((1, 's'))
pass_tuple([])  # type error


def get_int_v1() -> int:
    return 1


def get_int_v2() -> int:
    return 1.0  # type error


def get_float_v1() -> float:
    return 1.0


def get_float_v2() -> float:
    return 1


def get_str() -> str:
    return 'text'
