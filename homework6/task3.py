def is_prime(number):
    if number < 2 or number > 1000:
        return False
    for i in range(2, int(pow(number, 0.5)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter number to check if its prime: "))
    if is_prime(num) == True:
        print(f'Number {num} is prime')
    else:
        print(f'Number {num} is not prime')
