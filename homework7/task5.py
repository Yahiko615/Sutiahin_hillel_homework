def my_all(iterable):
    for element in iterable:
        if not bool(element):
            return False
    return True


numbers_list = [1, 2, 3, 4, 5]
mixed_list = [None, "some string", False, 20, object]
empty_list = []
print(my_all(numbers_list))
print(my_all(mixed_list))
print(my_all(empty_list))
