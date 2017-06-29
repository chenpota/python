from typing import TYPE_CHECKING, Optional, Union
#######################################


def this_is_a_function_to_be_barabara1(v: Union[Union[int, str, Optional[int]], Union[int, str, Optional[int]]]) -> None:
    pass
#######################################


MYTYPE = Union[
    Union[int, str, Optional[int]],
    Union[int, str, Optional[int]]]


def this_is_a_function_to_be_barabara2(v: MYTYPE) -> None:
    pass
#######################################


if TYPE_CHECKING:
    MYTYPE2 = Union[
        Union[int, str, Optional[int]],
        Union[int, str, Optional[int]]]


def this_is_a_function_to_be_barabara3(v: 'MYTYPE2') -> None:
    pass
