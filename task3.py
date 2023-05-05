omnivores = {'Bob', 'Charlie'}
vegetarians = {'Alice', 'Eve', 'Frank'}
# Didn't quite understand the assignment,
# it turns out that omnivores can eat both and eat vegetables and herbs,
# and vegetarians eat vegetables and herbs,
# so I understand correctly that I just need to combine these two groups?
vegetarian_guests = omnivores | vegetarians
# I decided just to display those who are in both groups since omnivores also eat vegetables and herbs
print('Vegetarian guests:', vegetarian_guests)
