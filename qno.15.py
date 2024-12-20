menu = {
    "pizza": 10,
    "burger": 7,
    "pasta": 8
}
option = input("Enter a menu option (pizza, burger, pasta): ")
if option in menu:
    price = menu[option]
    print(f"The price of {option} is ${price}.")
else:
    print("Invalid menu option. Please enter pizza, burger, or pasta.")
