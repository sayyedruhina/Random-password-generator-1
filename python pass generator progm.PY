import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Build character pool based on user choices
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if use_numbers:
        characters += string.digits  # 0-9
    if use_symbols:
        characters += string.punctuation  # !@#$%^&*...
    
    # Validation: Check if at least one option is selected
    if not characters:
        return "Error: Please select at least one character type"
    
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main Program
print("=== Random Password Generator ===")

try:
    # Get user input
    length = int(input("Enter password length: "))
    
    # Input validation for length
    if length < 4:
        print("Password length should be at least 4")
    else:
        letters = input("Include letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        # Generate and display password
        result = generate_password(length, letters, numbers, symbols)
        print(f"\nGenerated Password: {result}")

except ValueError:
    print("Error: Please enter a valid number for length")