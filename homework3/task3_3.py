friends = ["John", "Marta", "James", "Artur"]
enemies = ["John", "Johnatan", "Artur", "James"]
# in tas
for friend in friends:
    if friend == "James":
        print(f"{friend} we are the best friends")
    elif friend in enemies:
        print(f"{friend} we are not friends anymore")
    else:
        print(f"{friend} we are the best friends")
