import re

camel_case_variables = ["FirstItem", "FriendsList", "MyTuple"]

snake_case_variables = []
for variable in camel_case_variables:
    # (?<!^) не возволяет заменить символы перед заглавной (?=[A-Z]) не позволяет заменить символы после строчной
    # тоесть разделяем FriendsList вот так Friends|List и | меняем на _
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', variable).lower()
    snake_case_variables.append(snake_case)

print(snake_case_variables)
