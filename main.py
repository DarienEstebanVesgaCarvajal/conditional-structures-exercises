try:
    number = int(input("what's the number?: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
    print("The number is invalid.")