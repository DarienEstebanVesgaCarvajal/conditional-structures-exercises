firstOperand = input("What's the first operand?: ")
operator = input("What's the operator ( +, -, *, /)?: ")
secondOperand = input("What's the second operand?: ")

firstOperand = float(firstOperand)
secondOperand = float(secondOperand)

if operator == "+":
    result = firstOperand + secondOperand
elif operator == "-":
    result = firstOperand - secondOperand
elif operator == "*":
    result = firstOperand * secondOperand
elif operator == "/":
    if secondOperand != 0:  # Check for division by zero
        result = firstOperand / secondOperand
    else:
        result = "Error: Division by zero."
else:
    result = "Error: Invalid operator."

print(f"{firstOperand} {operator} {secondOperand} = {result}")