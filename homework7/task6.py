def count_arrow(string):
    arrow_count = [string.count('^'), string.count('v'), string.count('<'), string.count('>')]
    max_count = max(arrow_count)
    total_arrow_count = len(string)
    min_variant = total_arrow_count - max_count
    return min_variant


print(count_arrow("^vv<v"))
print(count_arrow("v>>>vv"))
print(count_arrow("<<<"))
