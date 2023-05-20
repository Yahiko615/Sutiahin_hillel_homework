def display_box(width: int, height: int, character="x"):
    box = f"{character * width}\n" + \
          f"{character}{(width - 2) * ' '}{character}\n" * (height - 2) + \
          f"{character * width}"
    print(box)


if __name__ == "__main__":
    display_box(4, 4)
    display_box(5, 4, 'x')
