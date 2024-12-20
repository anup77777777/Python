char = input("Enter a character: ").lower()
if char.isalpha() and len(char) == 1:
    
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Error!!. Please enter a single alphabet character.")
