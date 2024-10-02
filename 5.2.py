while True:
    first_number = int(input("Enter a first number: "))
    action = input("Enter a calculation(+, -, *, /): ")
    second_number = int(input("Enter a second number: "))
    if action == "+":
        result = first_number + second_number
        print(result)
    elif action == "-":
        result = first_number - second_number
        print(result)
    elif action == "*":
        result = first_number * second_number
        print(result)
    elif action == "/":
        if second_number == 0:
            print("Error")
        else:
            result = first_number / second_number
            print(result)
    continue_or_quit = input("yes/y if you want continue or quit/q if you want to end calculation: ")
    if continue_or_quit == "quit" or continue_or_quit == "q":
        print("Calculation is end")
        break
    elif continue_or_quit == "yes" or continue_or_quit == "y":
        continue