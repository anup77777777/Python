a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
operator = input("Enter operators (+, -, *, /): ")
if operator == "+":
    result = a + b
elif operator == "-":
    result = a- b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        result = "undefined (division by zero)"
else:
    result = "Invalid operator"
print(f"Your Answer is: {result}")
