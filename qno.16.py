temperature = float(input("Enter the temperature : "))
if temperature > 30:
    advice = "It's hot, stay hydrated!"
elif 15 <= temperature <= 30:
    advice = "Enjoy the weather!"
else:
    advice = "It's cold, wear warm clothes!"
print(advice)
