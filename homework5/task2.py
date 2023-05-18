import pickle

with open('test/data/tuples.txt', 'r+b') as file:
    data_tuple = pickle.load(file)
count = 0
for item in data_tuple:
    count += 1
    element1 = item[0]
    element2 = item[1]
    operation = item[2]
    if operation == 1:
        operation = '+'
        result = element1 + element2
    elif operation == 2:
        operation = '-'
        result = element1 - element2
    elif operation == 3:
        operation = '*'
        result = element1 * element2
    print(f'Result of the {count} operation: {element1}{operation}{element2}={result}')
