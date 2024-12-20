color = input("Enter a color (red, yellow, green): ")
if color == "red":
    action = "Stop"
elif color == "yellow":
    action = "Get Ready"
elif color == "green":
    action = "Go"
else:
    action = "Invalid color"
print(f"The action for {color} is: {action}")
