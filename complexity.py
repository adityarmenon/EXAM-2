def complex(password):
    rating = 0
    if len(password) >= 8:
        rating += 1
    if len(password) >= 12:
        rating += 1
    if any(char.islower() for char in password):
        rating += 1
    if any(char.isupper() for char in password):
        rating += 1
    if any(char in "!@#$%^&*()_+" for char in password):
        rating += 1
    if any(char.isdigit() for char in password):
        rating += 1
    if rating >=5:
        return "Strong"
    if rating < 5:
        return "Weak"

password = input("Enter the password: ")
b = complex(password)
print("Strength is: ", b)
