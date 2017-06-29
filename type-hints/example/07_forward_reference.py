from typing import Optional
#######################################


class BinaryTree(object):

    def __init__(
            self,
            left: Optional['BinaryTree'],
            right: Optional['BinaryTree']) -> None:
        self._left = left
        self._right = right

    def do_something(v: 'BinaryTree') -> None:
        pass

left = BinaryTree(None, None)
right = BinaryTree(None, None)
root1 = BinaryTree(left, right)
root2 = BinaryTree(left, 3)  # error
