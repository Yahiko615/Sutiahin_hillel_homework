def calculate_sum(*args):
    return sum(args)


if __name__ == "__main__":
    result = calculate_sum(23, 41, 42, 4, 14, 14, 15, 51, 51, 512, 55, 21, 412, 5125, 125, 32, 225, 1, 521, 52, 624, 63,
                           76, 34574, 5)
    print(f'Sum of the args: {result}')
