import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie!'

    #r>s, s>p, p>r
    if is_win(user, computer):
        return "You won!"

    return 'You Lost!'

def is_win(player, opponent):
    print(f"user: {player}")
    print(f"computer: {opponent}")
    # return true if player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def main():
    print(play())


if __name__ == "__main__":
    main()
