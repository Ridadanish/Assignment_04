import random
import string

def generate_password(length):
    if length < 4:
        return "⚠️ Password length should be at least 4 characters."

    # Ensure the password includes at least one lowercase, one uppercase, one digit, and one special character.
    password_chars = [
        random.choice(string.ascii_lowercase),  # Lowercase letter
        random.choice(string.ascii_uppercase),  # Uppercase letter
        random.choice(string.digits),           # Digit
        random.choice(string.punctuation)       # Special character
    ]

    # Combine all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # Add random characters to reach the desired length
    password_chars += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password_chars)
    return "".join(password_chars)

def main():
    print("🔐 Welcome to the Ultimate Password Generator! 🔒")
    try:
        length = int(input("👉 Enter desired password length (min 4): "))
        print("\n⏳ Generating your secure password...")
        password = generate_password(length)
        print(f"\n📝 Your Generated Password: {password}")
        print("\n💡 Tip: Store your password safely and never share it with anyone!")
    except ValueError:
        print("⚠️ Oops! Please enter a valid number.")

if __name__ == "__main__":
    main()