
# Writing a program that propmt user for their name and its then written in a file
print("Write your name and i will write it in a file for you")
name = input("What is your name?")

# Writing the response above in a file
file_name = "display_name.txt"
with open(file_name, "w") as object_file:
    object_file.write(name)
