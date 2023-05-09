number = 2
# idk about 2 different way, i've done it with four so you can decide if some of them are right

multiply1_result1 = number * 2
multiply1_result2 = number + number
multiply1_result3 = number << 1
multiply1_result4 = pow(number, 2)
# i mean some of them is not multiply exactly but contains the same result, im talking about things like pow(), it
# is not exactly multiplication, but it contains the same result,
# and according to the assignment I was supposed to get a result 4 and that's exactly the result I got when I did it
divide_result1 = number / 2
divide_result2 = number // 2
divide_result3 = number >> 1
divide_result4 = number % 2
# % is modulo division, but it is still one different way to divide
multiply_results = [multiply1_result1, multiply1_result2, [multiply1_result3, bin(multiply1_result3)],
                    multiply1_result4]
divide_results = [divide_result1, divide_result2, [divide_result3, bin(divide_result3)],
                  divide_result4]
for index, value in enumerate(multiply_results):
    print(f'Multiply way {index+1} result: {value}')

for index, value in enumerate(divide_results):
    print(f'Divide way {index+1} result: {value}')
