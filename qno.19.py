correct_username = "admin"
correct_password = "password123"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == correct_username and password == correct_password:
    print("Access Granted")
else:
    print("Access Denied")
