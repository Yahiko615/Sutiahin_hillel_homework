import re

with open('text.txt', 'r') as file:
    text = file.read()

sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
print(sentences)
