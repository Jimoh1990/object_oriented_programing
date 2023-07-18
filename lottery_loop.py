import random
#initilising your list of items
ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

# creating an empty list to collect the items choosen
selected_items = []
# iterate 4 times using loop to select each choice and add it to the empty list
for i in range(4):
    random_item = random.choice(ticket)
    selected_items.append(random_item)
print(selected_items)
