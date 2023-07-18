# Writing a program that prompt for user input

while True:
    print("Enter two numbers and i will give you the addition(enter q to quit)")
    try:
        a = input("first number: ")
        if a == "q":
            break
        b = input("second number: ")
        if b == "q":
            break
        a = int(a)
        b = int(b)
    except ValueError:
        print("please enter numerical data")
    else:
        answer = a + b
        print(answer)
