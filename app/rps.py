# the "app/rps.py" file...

from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"]

def determine_winner(u, c):
    if u == "rock" and c == "rock":
        return "TIE GAME"
    elif u == "rock" and c == "paper":
        return "COMPUTER WINS"
    elif u == "rock" and c == "scissors":
        return "USER WINS"
    elif u == "paper" and c == "rock":
        return "USER WINS" # OOPS
    elif u == "paper" and c == "paper":
        return "TIE GAME"
    elif u == "paper" and c == "scissors":
        return "COMPUTER WINS" # OOPS
    elif u == "scissors" and c == "rock":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "paper":
        return "USER WINS"
    elif u == "scissors" and c == "scissors":
        return "TIE GAME"


if __name__ == "__main__":

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    winner = determine_winner(u, c)
    print(winner)