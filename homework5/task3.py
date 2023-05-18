import re

file_path = 'text.txt'

with open(file_path, 'r') as file:
    text = file.read().lower()

letter_counts = {}
for letter in re.findall(r'[a-z]', text):
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

# print(letter_counts.items())

for letter, count in letter_counts.items():
    print(f"'{letter}' appears {count} times")
