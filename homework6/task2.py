def square(square_side):
    perimeter = 4 * square_side
    area = pow(square_side, 2)
    diagonal = pow(2, 0.5) * square_side
    return perimeter, area, diagonal


if __name__ == "__main__":
    side = int(input("Enter square side length: "))
    perimeter_result, area_result, diagonal_result = square(side)
    print("Perimeter:", perimeter_result)
    print("Area:", area_result)
    print("Diagonal:", diagonal_result)
