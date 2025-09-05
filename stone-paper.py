# stone_paper.py
import random

CHOICES = {
    "s": "Stone",
    "p": "Paper",
    "c": "Scissors"  # using 'c' for Scissors to avoid clash with 's'
}

# Who beats whom
WINS_AGAINST = {
    "s": "c",  # Stone crushes Scissors
    "p": "s",  # Paper covers Stone
    "c": "p"   # Scissors cut Paper
}

def get_user_choice():
    while True:
        user = input("Choose [s]tone, [p]aper, s[c]issors (or 'q' to quit): ").strip().lower()
        if user == "q":
            return "q"
        if user in CHOICES:
            return user
        print("Invalid choice. Please enter s, p, or c (or q to quit).")

def get_computer_choice():
    return random.choice(list(CHOICES.keys()))

def decide_round(user, comp):
    if user == comp:
        return "tie"
    return "win" if WINS_AGAINST[user] == comp else "lose"

def main():
    print("=== Stone–Paper–Scissors ===")
    print("First to 3 points wins the match. Type 'q' anytime to quit.\n")

    user_score = 0
    comp_score = 0

    while user_score < 3 and comp_score < 3:
        user = get_user_choice()
        if user == "q":
            print("You quit the game. Bye!")
            return

        comp = get_computer_choice()
        result = decide_round(user, comp)

        print(f"You: {CHOICES[user]} | Computer: {CHOICES[comp]}")
        if result == "tie":
            print("Result: It's a tie! No points.\n")
        elif result == "win":
            user_score += 1
            print("Result: You win this round!\n")
        else:
            comp_score += 1
            print("Result: You lose this round.\n")

        print(f"Score → You {user_score} : {comp_score} Computer\n")

    if user_score > comp_score:
        print("🏆 You won the match! GG!")
    else:
        print("🤖 Computer won the match. Better luck next time!")

if __name__ == "__main__":
    main()
