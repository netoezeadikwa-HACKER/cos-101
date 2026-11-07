user_input = input("Enter a number between 1 and 12 (or e to quit): ")

while user_input != "e":
    number = int(user_input)
    while number <= 1:
        print("Invalid number! Number cannot be less than 1.")
        user_input = input("Enter another number (or e to quit): ")
        if user_input == "e":                                                   
            break
        number = int(user_input)
    if user_input == "e":
        break
    if number > 1 and number <= 12:
        print("This is the multiplication table of", number)
        for i in range(1, 13):
            print(number, "x", i, "=", number * i)
    elif number > 12:
        print("Number is greater than 12.")
    user_input = input("Enter another number (or e to quit): ")

print("Multiplication cancled :( ")





























































































































