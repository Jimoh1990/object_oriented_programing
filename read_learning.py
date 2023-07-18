# Approach one to print the file once by reading the entire contents
file_name = "learning_python.txt"
with open(file_name) as object_file:
    contents = object_file.read()
modified_contents = contents.replace("python", "java")
print(modified_contents)

# Approach two to print the file once by looping throgh each line in the file
fileName = "learning_python.txt"
with open(file_name) as object_file:
    for line in object_file:
        modified_line = line.replace("python","java")
        print(modified_line.rstrip())
print()

# Approach three to print the contents once by storing each line i a list for it to be worked on outside the block
file_name = "learning_python.txt"
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    modified_line = line.replace("python", "java")
    print(modified_line.strip())
