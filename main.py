from time import localtime

currentTime = localtime()
currentDay = currentTime.tm_mday
currentMonth = currentTime.tm_mon
currentYear = currentTime.tm_year

birthDay = input("What's your birth day?: ")
birthMonth = input("What's your birth month?: ")
birthYear = input("What's your birth year?: ")

birthDay = int(birthDay)
birthMonth = int(birthMonth)
birthYear = int(birthYear)

age = currentYear - birthYear

if (currentMonth < birthMonth) or (currentMonth == birthMonth and currentDay < birthDay):
    age -= 1

print(f"You are {age} years old.")