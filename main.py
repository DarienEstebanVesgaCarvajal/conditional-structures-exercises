sideA = float(input("What's the length of side A?: "))
sideB = float(input("What's the length of side B?: "))
sideC = float(input("What's the length of side C?: "))

if sideA + sideB <= sideC or sideA + sideC <= sideB or sideB + sideC <= sideA:
    print("Not a valid triangle.")
else:
    if sideA == sideB == sideC:
        print("The triangle is equilateral.")
    elif sideA == sideB or sideA == sideC or sideB == sideC:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")