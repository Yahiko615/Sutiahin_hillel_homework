elements = [1, 2, 3, 4, 5, 6, 7, 8]

for element in elements:
    print(element)

odd_numbers = []
even_numbers = []

for index, value in enumerate(elements):
    if index % 2 != 0:
        odd_numbers.append((index, value))
    else:
        even_numbers.append((index, value))

print(f'Odd:  {odd_numbers}')
print(f'even:  {even_numbers}')
