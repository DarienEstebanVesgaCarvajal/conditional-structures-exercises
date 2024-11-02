firstNumber = input("What's the first number? ")
secondNumber = input("What's the second number? ")
thirdNumber = input("What's the third number? ")
fourthNumber = input("What's the fourth number? ")

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)
thirdNumber = int(thirdNumber)
fourthNumber = int(fourthNumber)

if firstNumber <= secondNumber and firstNumber <= thirdNumber and firstNumber <= fourthNumber:
    if secondNumber <= thirdNumber and secondNumber <= fourthNumber:
        if thirdNumber <= fourthNumber:
            print(f"{firstNumber} {secondNumber} {thirdNumber} {fourthNumber}")
        else:
            print(f"{firstNumber} {secondNumber} {fourthNumber} {thirdNumber}")
    elif thirdNumber <= secondNumber and thirdNumber <= fourthNumber:
        if secondNumber <= fourthNumber:
            print(f"{firstNumber} {thirdNumber} {secondNumber} {fourthNumber}")
        else:
            print(f"{firstNumber} {thirdNumber} {fourthNumber} {secondNumber}")
    else:
        if secondNumber <= thirdNumber:
            print(f"{firstNumber} {fourthNumber} {secondNumber} {thirdNumber}")
        else:
            print(f"{firstNumber} {fourthNumber} {thirdNumber} {secondNumber}")
elif secondNumber <= firstNumber and secondNumber <= thirdNumber and secondNumber <= fourthNumber:
    if firstNumber <= thirdNumber and firstNumber <= fourthNumber:
        if thirdNumber <= fourthNumber:
            print(f"{secondNumber} {firstNumber} {thirdNumber} {fourthNumber}")
        else:
            print(f"{secondNumber} {firstNumber} {fourthNumber} {thirdNumber}")
    elif thirdNumber <= firstNumber and thirdNumber <= fourthNumber:
        if firstNumber <= fourthNumber:
            print(f"{secondNumber} {thirdNumber} {firstNumber} {fourthNumber}")
        else:
            print(f"{secondNumber} {thirdNumber} {fourthNumber} {firstNumber}")
    else:
        if firstNumber <= thirdNumber:
            print(f"{secondNumber} {fourthNumber} {firstNumber} {thirdNumber}")
        else:
            print(f"{secondNumber} {fourthNumber} {thirdNumber} {firstNumber}")
elif thirdNumber <= firstNumber and thirdNumber <= secondNumber and thirdNumber <= fourthNumber:
    if firstNumber <= secondNumber and firstNumber <= fourthNumber:
        if secondNumber <= fourthNumber:
            print(f"{thirdNumber} {firstNumber} {secondNumber} {fourthNumber}")
        else:
            print(f"{thirdNumber} {firstNumber} {fourthNumber} {secondNumber}")
    elif secondNumber <= firstNumber and secondNumber <= fourthNumber:
        if firstNumber <= fourthNumber:
            print(f"{thirdNumber} {secondNumber} {firstNumber} {fourthNumber}")
        else:
            print(f"{thirdNumber} {secondNumber} {fourthNumber} {firstNumber}")
    else:
        if firstNumber <= secondNumber:
            print(f"{thirdNumber} {fourthNumber} {firstNumber} {secondNumber}")
        else:
            print(f"{thirdNumber} {fourthNumber} {secondNumber} {firstNumber}")
else:
    if firstNumber <= secondNumber and firstNumber <= thirdNumber:
        if secondNumber <= thirdNumber:
            print(f"{fourthNumber} {firstNumber} {secondNumber} {thirdNumber}")
        else:
            print(f"{fourthNumber} {firstNumber} {thirdNumber} {secondNumber}")
    elif secondNumber <= firstNumber and secondNumber <= thirdNumber:
        if firstNumber <= thirdNumber:
            print(f"{fourthNumber} {secondNumber} {firstNumber} {thirdNumber}")
        else:
            print(f"{fourthNumber} {secondNumber} {thirdNumber} {firstNumber}")
    else:
        if firstNumber <= secondNumber:
            print(f"{fourthNumber} {thirdNumber} {firstNumber} {secondNumber}")
        else:
            print(f"{fourthNumber} {thirdNumber} {secondNumber} {firstNumber}")