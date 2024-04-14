import random

def get_correct_positions(secret_number, guess):
    return sum(1 for x, y in zip(secret_number, guess) if x == y)

def get_correct_digits(secret_number, guess):
    return sum(min(secret_number.count(digit), guess.count(digit)) for digit in set(secret_number))

def player1_turn():
    secret_number = input("Player 1, enter a {}-digit number: ".format(num_digits))
    while len(secret_number) != num_digits or not secret_number.isdigit():
        secret_number = input("Invalid input. Please enter a {}-digit number: ".format(num_digits))
    return secret_number

def player2_turn():
    guess = input("Player 2, enter your guess ({} digits): ".format(num_digits))
    while len(guess) != num_digits or not guess.isdigit():
        guess = input("Invalid input. Please enter {}-digit number: ".format(num_digits))
    return guess

def play_game():
    global winner
    while True:
        player1_number = player1_turn()
        attempts_p2 = 0
        while True:
            attempts_p2 += 1
            guess_p2 = player2_turn()
            if guess_p2 == player1_number:
                print("Congratulations, Player 2! You guessed the number in {} attempts.".format(attempts_p2))
                winner = "Player 2"
                return
            else:
                correct_positions = get_correct_positions(player1_number, guess_p2)
                correct_digits = get_correct_digits(player1_number, guess_p2)
                print("Incorrect guess. Correct positions: {}. Correct digits: {}.".format(correct_positions, correct_digits))

num_digits = 4
winner = None

while True:
    play_game()
    print("Player 1's turn now.")
    play_game()
    if winner == "Player 2":
        print("Player 2 wins!")
        break
    else:
        print("Player 1 wins!")
        break
