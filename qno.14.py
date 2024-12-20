age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))
if age > 18 and experience >= 2:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"
print(f"You are {eligibility} for the job.")
