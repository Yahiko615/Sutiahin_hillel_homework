friends = ["John", "Marta", "James", "Artur"]
enemies = ["John", "Johnatan", "Artur", "James"]

for friend in friends:
    if friend == "James":
        continue
    elif friend in enemies:
        print(f"{friend} we are not friends anymore")
    else:
        print(f"{friend} we are the best friends")
