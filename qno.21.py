salary = int(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if salary >= 50000 and credit_score >= 700:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"
print(f"You are {eligibility} for the car loan.")
