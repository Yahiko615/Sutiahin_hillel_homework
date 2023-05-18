import os
import pickle
import random

# с exist_ok=True не выдает ошибки, файл просто перезаписывается если уже существует
os.makedirs('test/data', exist_ok=True)

data_tuple = []
for _ in range(100):
    element1 = random.randint(1, 100)
    element2 = random.randint(1, 100)
    element3 = random.randint(1, 3)
    data_tuple.append((element1, element2, element3))

with open('test/data/tuples.txt', 'w+b') as file:
    pickle.dump(data_tuple, file)
