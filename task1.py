eleks_employees = ['Misha', 'Dima', 'Marina']
toshiba_employees = ['Alex', 'Den', 'Marina']

toshiba_employees.extend(eleks_employees)
eleks_employees.clear()
print(eleks_employees)
print(toshiba_employees)
