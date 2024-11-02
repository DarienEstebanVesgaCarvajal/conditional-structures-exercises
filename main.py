firstWord = input("First word: ")
secondWord = input("Second word: ")

firstLength = len(firstWord)
secondLength = len(secondWord)

if firstLength > secondLength:
    difference = firstLength - secondLength
    print(f"The word '{firstWord}' is {difference} letters longer than '{secondWord}'.")
elif secondLength > firstLength:
    difference = secondLength - firstLength
    print(f"The word '{secondWord}' is {difference} letters longer than '{firstWord}'.")
else:
    print("Both words are the same length.")