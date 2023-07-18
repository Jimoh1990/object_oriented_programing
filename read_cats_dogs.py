# Program that reads two different text filea
file_names = ["cats.txt", "dogs.txt"]
for file_name in file_names:
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
       pass
    else:
        print(contents)
