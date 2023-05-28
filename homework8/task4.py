import sys

result_1 = [num for num in range(1, 1001) if num // 10 % 10 == 3 or num % 10 == 3]
result_2 = (num for num in range(1, 1001) if num // 10 % 10 == 3 or num % 10 == 3)
print(result_1)
for number in result_2:
    print(number)
print(f'Size of {type(result_1)} = {sys.getsizeof(result_1)}')
print(f'Size of {type(result_2)} = {sys.getsizeof(result_2)}')
