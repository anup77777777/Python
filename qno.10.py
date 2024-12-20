marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
elif marks < 70:
    grade = "Fail"
else:
    grade = "Invalid marks"
print(f"Your grade is: {grade}")
