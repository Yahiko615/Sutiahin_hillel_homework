import re
from typing import Callable, Any, List


def custom_filter(callback: Callable[[Any], bool], sequence: List[Any]) -> List[Any]:
    """Custom filter function."""
    filtered_list = []
    for item in sequence:
        if callback(item):
            filtered_list.append(item)
    return filtered_list


def has_vowel(word):
    pattern = r'[aeiou]'
    return re.findall(pattern, word, re.IGNORECASE) != []


def is_even(num):
    return num % 2 == 0


def is_positive(num):
    return num > 0


vowels = ['a', 'e', 'i', 'o', 'u']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
floats = [0.5, -1.2, 3.7, -2.8, 4.1, -0.9, 5.6]
strings = ['mrtwwd', 'plkj', 'rsts', 'qwrr', 'lmna', 'xyz', 'vbanwa', 'cvb', 'jkql', 'dfqqg']

print(custom_filter(is_even, numbers))
# print(custom_filter(lambda x: x % 2 == 0, numbers))
print(custom_filter(is_positive, floats))
# print(custom_filter(lambda x: x > 0, floats))
print(custom_filter(has_vowel, strings))
# print(custom_filter(lambda x: any(char.lower() in vowels for char in x), strings))
