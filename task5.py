names = ['John Dow', 'John Dow', 'Marta Dow']
unique_dict = dict.fromkeys(names)
# print(unique_dict)
unique_names_list = list(unique_dict.keys())

print('List of non-duplicate names:', unique_names_list)
