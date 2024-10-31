try:
    userInput = int(input("What's the number?: "))
    if userInput % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
    print("The number is invalid.")
