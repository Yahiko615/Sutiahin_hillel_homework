import re


def remove_numbers_from_file(file_path):
    pattern = r'\d+'
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            line_without_numbers = re.sub(pattern, '', line)
            file.write(line_without_numbers)
        file.truncate()


if __name__ == "__main__":
    remove_numbers_from_file('text.txt')
