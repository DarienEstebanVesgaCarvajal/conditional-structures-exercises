year = int(input("What's yhe year?: "))

if year >= 1582: # G
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"The {year} year is a leap.")
    else:
          print(f"The {year} year isn't a leap.")
else:# J
    if year %4 == 0:
            print(f"The {year} year is a leap.")
    else:
        print(f"The {year} year isn't a leap.")