months = {1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"}
number = int(input("Enter a number in the range of 1 to 12: "))
if 1 <= number <= 12:
    print(f"The number {number} is {months[number]}")
else:
    print("Error: The number must be in the range of 1 to 12.")
