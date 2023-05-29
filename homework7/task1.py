import os


def custom_print(*args, sep=' ', end='\n'):
    """Custom print function. Working with all operating systems"""
    output = sep.join(str(arg) for arg in args) + end
    os.write(1, output.encode())


# def print(self, *args, sep=' ', end='\n', file=None):
#     pass


print('Hello, Misha!')
custom_print("Hello, Misha!")
custom_print("Hello", "Misha", sep=", ", end="!")
