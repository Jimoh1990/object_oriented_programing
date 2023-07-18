while True:
    name = input("Enter your name (or 'q' to quit): ")
    if name == 'q':
        break

    # Print greeting to the screen
    print(f"Welcome, {name}!")

    # Write the visit entry to the guest_book.txt file
    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")

print("Guest entries recorded in guest_book.txt file.")
