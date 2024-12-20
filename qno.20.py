
month = int(input("Enter a month number (1–12): "))
if month in [12, 1, 2]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
elif month in [9, 10, 11]:
    season = "Autumn"
else:
    season = "Invalid month number"
print(f"The season for month number {month} is: {season}")
