# Writing a poll about people's reasons for loving programing
while True:
    response = input("Why do you guys like programming. (enter q to quit)?:" )
    if response == "q":
        break

    # Storing their responses for later used
    writing_file = "programming_poll.txt"
    with open(writing_file, "a") as object_file:
        object_file.write(f" {response}\n")

print("The pole as ended and response saved in progamming_poll.txt")    
