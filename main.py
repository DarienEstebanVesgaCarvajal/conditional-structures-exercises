firstNumber = input("What's the first number? ")
secondNumber = input("What's the second number? ")
thirdNumber = input("What's the third number? ")

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)
thirdNumber = int(thirdNumber)

if firstNumber <= secondNumber and firstNumber <= thirdNumber:
    if secondNumber <= thirdNumber:
        print(f"{firstNumber} {secondNumber} {thirdNumber}")
    else:
        print(f"{firstNumber} {thirdNumber} {secondNumber}")
elif secondNumber <= firstNumber and secondNumber <= thirdNumber:
    if firstNumber <= thirdNumber:
        print(f"{secondNumber} {firstNumber} {thirdNumber}")
    else:
        print(f"{secondNumber} {thirdNumber} {firstNumber}")
else:
    if firstNumber <= secondNumber:
        print(f"{thirdNumber} {firstNumber} {secondNumber}")
    else:
        print(f"{thirdNumber} {secondNumber} {firstNumber}")