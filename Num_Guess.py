import random
from Score import ScoreManager

p = 1
score = ScoreManager()
print("🎯 Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100... Can you guess it?")

def play_game():
    print("\nChoose your difficulty: Easy (10 attempts) or Hard (5 attempts)")

    # Difficulty setting
    d = input("Enter difficulty (Easy/Hard) : ").strip().lower()
    a = 10 if d == "easy" else 5
    while True:
        if d not in ["easy", "hard"]:
            print("⚠️ Invalid difficulty. Please choose 'Easy' or 'Hard'.")
            d = input("Enter difficulty (Easy/Hard) : ").strip().lower()
            a = 10 if d == "easy" else 5
        else:
            break

    # Generate the number
    sn = random.randint(1, 100)

    # Game loop
    while a > 0:
        print(f"\nYou have {a} attempts remaining.")
        try:
            g = int(input("Make a guess : "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if g == sn:
            print(f"🎉 Congrats! You guessed it right. The number was {sn}.")
            points = p * 10  # Reward: more attempts left = more points
            score.add_points(points)
            print(f"You earned {points} points!")
            break
        elif g < sn:
            print("🔼 Too low!")
        else:
            print("🔽 Too high!")
        a -= 1
    

    # If user fails
    if a == 0 and g != sn:
        print(f"\n💀 You've run out of guesses. The number was {sn}. Better luck next time!")
        print("🕹️ Game Over")

# 🎮 Main Loop
while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("\n🎯 Final Score:", score.get_score())
        if score.update_high_score():
            print("🎉 New High Score:", score.get_high_score())
        else:
            print("🏆 High Score remains:", score.get_high_score())
        print("👋 Thanks for playing! See you next time.")
        break