import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Define character pools based on user preferences
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Ensure at least one character from each category
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Generate remaining characters
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(characters))

    # Shuffle the password to ensure randomness
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
        use_digits = input("Include digits? (y/n): ").lower() == "y"
        use_special = input("Include special characters? (y/n): ").lower() == "y"

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
