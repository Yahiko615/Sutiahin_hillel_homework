def print_function_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"You have called function named: '{func.__name__}'.")
        return result

    return wrapper


@print_function_name
def summation(a, b):
    return a + b


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 1: "))
print(f'Result of the summation of {num1} and {num2} =', summation(num1, num2))
