def max_custom(lst, amount=1):
    if amount <= 0:
        return []

    if amount == 1:
        max_value = lst[0]
        for num in lst:
            if num > max_value:
                max_value = num
        return max_value

    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[:amount]


def min_custom(lst, amount=1):
    if amount <= 0:
        return []

    if amount == 1:
        min_value = lst[0]
        for num in lst:
            if num < min_value:
                min_value = num
        return min_value

    sorted_lst = sorted(lst)
    return sorted_lst[:amount]


numbers = [1, 2, 3, 4, 5, 6, 12, 0, 8, 9]
strings = ["111", "1111", "aaaa"]
print(max_custom(numbers, 3))
print(max_custom(strings, 2))
print(min_custom(numbers, 3))
print(min_custom(strings, 2))
