dividend = int(input("What's the dividend?: "))
divisor = int(input("What's the divisor?: "))

if divisor == 0:
    print("Error: Division by zero is undefined.")
else:
    quotient = dividend // divisor
    remainder = dividend % divisor

    if remainder == 0:
        print("The division is exact.")
    else:
        print("The division isn't exact.")
    
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")