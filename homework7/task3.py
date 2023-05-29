from typing import Callable, TypeVar, Sequence

T = TypeVar('T')
U = TypeVar('U')


def my_map(callback: Callable[[T], U], sequence: Sequence[T]) -> Sequence[U]:
    """
   Applies a callback function to each element of the sequence and returns a new sequence
    containing the results.

    """
    return [callback(element) for element in sequence]


numbers = [1, -2, 3, -4.8, 5]
# print(list(map(lambda x: pow(x, 2), numbers)))
print(my_map(lambda x: pow(x, 2), numbers))
print(my_map(lambda x: abs(x), numbers))
print(my_map(lambda x: str(x), numbers))
