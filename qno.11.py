age = int(input("Enter the  age: "))
if age < 13:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teenager"
else:
    category = "Adult"
print(f"The person is a {category}")
