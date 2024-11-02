character = input("What's the character?: ")

if character.isdigit():
    print("It's a number.")
elif character.isalpha():
    if character.isupper():
        print("It's an uppercase letter.")
    else:
        print("It's a lowercase letter.")
else:
    print("It's neither a letter nor a number.")