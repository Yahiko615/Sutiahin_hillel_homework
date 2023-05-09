elements = [1, 2, 3, 4, 5, 6, 7, 8]

for element in elements:
    print(element)

odd_numbers = []
even_numbers = []
# or we can just use enumerate(elements), instead of zip(range(len(elements)), elements), but we didnt used it in lesson
# so i decided to use zip, range and len to show how i did it using them
for index, value in zip(range(len(elements)), elements):
    if index % 2 != 0:
        odd_numbers.append((index, value))
    else:
        even_numbers.append((index, value))

print(f'Odd:  {odd_numbers}')
print(f'even:  {even_numbers}')
