import re

string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"

pattern = re.compile(r'([^=&]+)=([^&^s{6}(?==)]*)')
matches = pattern.findall(string)

result_dict = {key: value for key, value in matches}

print(result_dict)
