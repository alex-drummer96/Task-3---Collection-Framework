from collections import Counter
from functools import lru_cache


class CustomTypeError(Exception):
    def __init__(self, data_type: type) -> None:
        self.data_type = data_type

    def __str__(self) -> str:
        return f'{self.data_type} is not allowed. Only string'


def check_type(string: str) -> None:
    if not isinstance(string, str):
        raise CustomTypeError(type(string))


@lru_cache(maxsize=None)
def count_unique_characters(string: str) -> int:
    check_type(string=string)
    letter_count = Counter(string)
    return len([key for key in letter_count if letter_count[key] == 1])
