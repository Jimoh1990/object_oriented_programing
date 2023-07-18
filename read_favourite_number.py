import json

# To read the contents of my json file and display the favourites number
file_name = "favourite_number.json"
with open(file_name) as f:
    contents = json.load(f)
    print(f"My favourites numbers are {contents}")
