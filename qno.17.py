height = float(input("Enter the player's height in feet: "))
if height >= 6:
    selection_status = "Selected"
else:
    selection_status = "Not Selected"

print(f"The player is {selection_status}")
