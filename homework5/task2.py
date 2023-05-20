import pickle

with open('test/data/tuples.txt', 'r+b') as file:
    data_tuple = pickle.load(file)

for index, item in enumerate(data_tuple):
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
    print(f'Result of the {index+1} operation: {element1}{operation}{element2}={result}')
