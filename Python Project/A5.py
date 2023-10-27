import random
import string


def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_digits = input(
        "Use digits in the password? (yes/no): ").lower() == "yes"
    use_special_chars = input(
        "Use special characters in the password? (yes/no): ").lower() == "yes"

    if use_digits or use_special_chars:
        password = generate_password(length, use_digits, use_special_chars)
        print(f"Generated Password: {password}")
    else:
        print("You must use at least digits or special characters for a secure password.")
