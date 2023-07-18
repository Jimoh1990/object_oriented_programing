import json

# Writing a program that print favourite number if already exist, if not, it create it
file_name = "favourite_number.json"
try:
    with open(file_name) as f:
        contents = json.load(f)
except FileNotFoundError:
    # Asking user to put his fafourite number
    favourite_number = []
    favourites_number = input("What are your fafourites number?: ")
    favourites_number = favourites_number.split()
    for numbers in favourites_number:
        favourite_number.append(int(numbers))
        file_name = "favourite_number.json"
        with open(file_name, "w") as f:
            json.dump(favourite_number, f)
else:
    print(f"The favourites numbers are {contents}")
