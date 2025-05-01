import random

# Dictionary with words and their hints
words_with_hints = {
    "encyclopedia": "📚 A book or resource with detailed information on many topics.",
    "photosynthesis": "🌿 Process plants use to convert sunlight into energy.",
    "architecture": "🏛️ The art and science of designing buildings.",
    "cryptography": "🔐 The study of secure communication techniques.",
    "philosophy": "🤔 The study of fundamental questions about existence and knowledge."
}

def print_hangman(attempts):
    """Display hangman status based on remaining attempts using emojis."""
    stages = {
        6: "😁 (All good!)",
        5: "🙂 (Keep it up!)",
        4: "😐 (Stay focused!)",
        3: "😟 (Be cautious!)",
        2: "😰 (Almost out!)",
        1: "😨 (Last chance!)",
        0: "💀 (Game Over!)"
    }
    print(f"Status: {stages[attempts]}")

# Select a random word and its hint
word, hint = random.choice(list(words_with_hints.items()))
guessed = []  # Letters that have been guessed
attempts = 6  # Total attempts

# Intro message
print("🎮 Hangman Challenge: Guess the Word!")
print(f"💡 Hint: {hint}")
print("\nWord: " + " ".join("_" for _ in word))
print_hangman(attempts)
print("\nGuessed letters: None\n")

# Main game loop
while attempts > 0:
    guess = input("🔤 Enter a letter: ").lower()

    if guess in guessed or len(guess) != 1 or not guess.isalpha():
        print("⚠️ Invalid or repeated guess. Try a different letter.\n")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"❌ Oops! '{guess}' is not in the word. Attempts left: {attempts}\n")
    else:
        print(f"✅ Good job! '{guess}' is in the word!\n")

    # Update display with guessed letters
    display = " ".join([letter if letter in guessed else "_" for letter in word])
    print("Word: " + display)
    print_hangman(attempts)
    print("Guessed letters: " + ", ".join(guessed) + "\n")

    # Check if the word is completely guessed
    if "_" not in display.replace(" ", ""):
        print(f"🏆 Congrats! You guessed the word '{word}' correctly! 🎉")
        break

# If attempts run out
if "_" in display.replace(" ", ""):
    print(f"💀 Game over! The word was '{word}'. Better luck next time! 🔄")