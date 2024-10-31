height = float(input("What's your height in meters?: "))
weight = float(input("What's your weight in kilograms?: "))
age = int(input("What's your age?: "))

bmi = weight / (height ** 2)

if age < 45:
    if bmi < 22.0:
        risk_condition = "low"
    else:
        risk_condition = "medium"
else:
    if bmi < 22.0:
        risk_condition = "medium"
    else:
        risk_condition = "high"

print(f"Your BMI is {bmi}. Your risk condition is {risk_condition}.")