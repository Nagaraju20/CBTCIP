import random

def main():
    while True:
        available_moves = ["Rock", "Paper", "Scissors"]
        computer_move = random.choice(available_moves)

        print("Computer has chosen its move.")
        print("Now it's your turn to choose. Good Luck!")

        while True:
            user_move = input("Please choose your move from these available moves: 'Rock' 'Paper' 'Scissors'\n"
                              "Enter the move you chose: ").strip().capitalize()
            if user_move in available_moves:
                break
            print("Invalid Move!! Please enter a move from the available moves only!")

        print("Computer chose:", computer_move)

        if user_move == computer_move:
            print("It's a tie!")
        elif (user_move == "Rock" and computer_move == "Scissors") or \
             (user_move == "Paper" and computer_move == "Rock") or \
             (user_move == "Scissors" and computer_move == "Paper"):
            print("You won! Congratulations!")
        else:
            print("Computer won! Better luck next time!")

        play_again = input("Do you want to play again? Type 'yes' or 'no': ").strip().lower()
        while play_again not in ['yes', 'no']:
            print("Invalid Input")
            play_again = input("Do you want to play again? Type 'yes' or 'no': ").strip().lower()

        if play_again == 'no':
            break

if __name__ == "__main__":
    main()
