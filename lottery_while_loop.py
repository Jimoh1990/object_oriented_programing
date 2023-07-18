import random

# Define the list containing numbers and letters
ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define your own ticket
my_ticket = [1, 'A', 5, 'B']

# Initialize the counter for the number of attempts
attempts = 0

# Keep pulling numbers until your ticket wins
while True:
    attempts += 1
    # Randomly select four numbers or letters
    selected_items = random.choices(ticket, k=4)
                       
    # Check if your ticket matches the selected items
    if set(selected_items) == set(my_ticket):
        break

# Print the number of attempts required to win
print(f"It took {attempts} attempts to win the lottery!")
