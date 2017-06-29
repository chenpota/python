from typing import NewType
#######################################


class INT(int):
    pass


class NEW_INT(INT):
    pass
#######################################


def pass_int(v: int) -> None:
    pass

pass_int(1)
pass_int(INT())
pass_int(NEW_INT())
#######################################


def pass_INT(v: INT) -> None:
    pass


pass_INT(1)  # error
pass_INT(INT())
pass_INT(NEW_INT())
#######################################


def pass_NEW_INT(v: NEW_INT) -> None:
    pass

pass_NEW_INT(1)  # error
pass_NEW_INT(INT())  # error
pass_NEW_INT(NEW_INT())
