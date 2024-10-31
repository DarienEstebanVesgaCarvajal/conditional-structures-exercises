firstNumber = input("What's the first number? ")
secondNumber = input("What's the second number? ")

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

if firstNumber < secondNumber:
    print(f"{firstNumber} {secondNumber}")
else:
    print(f"{secondNumber} {firstNumber}")