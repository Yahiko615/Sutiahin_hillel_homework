import re


def remove_vowels(input_string):
    return re.sub(r'[aeiouAEIOU]', '', input_string)


if __name__ == "__main__":
    str_name = 'Misha'
    print(remove_vowels(str_name))
    print(remove_vowels("Misha"))
