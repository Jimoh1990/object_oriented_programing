import random

# Creating list of series of 10 numbers and 5 letters
ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
# randomly select four numbers or letters
selected_items = random.choices(ticket, k = 4)

# print the selected items
print("Selected items:", selected_items)

# check if any ticket matches the selected_items
if set(selected_items).issubset(set(ticket)):
    print("Congratulations you have winning tickets")
else:
    print("Sorry, your ticket did not win this time")
