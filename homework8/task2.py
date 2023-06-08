def even_squares_gen():
    for number in range(0, 1000000001, 2):
        yield number ** 2


my_custom_gen = even_squares_gen()
print(type(my_custom_gen))
for num in my_custom_gen:
    print(num)
