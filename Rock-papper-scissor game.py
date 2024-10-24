import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # User input
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Computer's random choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # Display user and computer choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine and display the winner
        result = determine_winner(user_choice, computer_choice)
        if result == "user":
            print("You win!")
        elif result == "computer":
            print("Computer wins!")
        else:
            print("It's a tie!")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
