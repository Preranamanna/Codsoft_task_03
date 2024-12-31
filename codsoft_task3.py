
import random
import string

def generate_password(length, complexity):
    characters = ""
    if complexity >= 1:
        characters += string.ascii_lowercase
    if complexity >= 2:
        characters += string.ascii_uppercase
    if complexity >= 3:
        characters += string.digits
    if complexity >= 4:
        characters += string.punctuation

    if not characters:
        raise ValueError("Complexity level must be between 1 and 4.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        complexity = int(input("Enter the complexity level (1-4): "))
        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
