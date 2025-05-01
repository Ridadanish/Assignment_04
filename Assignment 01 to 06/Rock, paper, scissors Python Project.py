import random
import time

choices = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
user_score = computer_score = 0
rounds = 0

print("🎲 Welcome to Rock, Paper, Scissors: Ultimate Showdown! 🚀")
print("🔔 Type 'q' anytime to quit.\n")

while True:
    user = input("👉 Choose your move (rock/paper/scissors): ").lower()
    if user == "q":
        print("\n🏆 Final Score:")
        print(f"   You: {user_score} | Computer: {computer_score}")
        print(f"   Total Rounds Played: {rounds}")
        print("👋 Thanks for playing! See you next time! 😊")
        break
    if user not in choices:
        print("⚠️ Oops! That's not a valid move. Please choose rock, paper, or scissors. 🚫\n")
        continue

    rounds += 1
    print("\n⏳ Computer is making its move...")
    time.sleep(1)  # Adding a slight delay for dramatic effect
    computer = random.choice(list(choices))
    print(f"🤖 Computer chose: {choices[computer]} ({computer.capitalize()})")

    if user == computer:
        print("🤝 It's a tie! Both moves are equal.")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        user_score += 1
        print("🎉 You win this round! Fantastic move! 🔥")
    else:
        computer_score += 1
        print("😢 You lost this round. Don't worry, keep trying! 💪")

    print(f"📊 Current Score: You {user_score} - {computer_score} Computer")
    print("------------------------------------------------\n")