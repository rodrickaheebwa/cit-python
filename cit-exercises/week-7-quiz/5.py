import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll(self):
        return random.choice([1,2,3,4,5,6])


def play(player1, player2):
    score1 = player1.roll()
    score2 = player2.roll()
    if score1 > score2:
        player1.score += 1
    elif score2 > score1:
        player2.score += 1

def game():
    player1 = Player("Alex")
    player2 = Player("Sam")
    while True:
        play(player1, player2)
        if player2.score >= 5:
            print(f"{player2.name} wins with a score of {player2.score}!")
            print("Game over!")
            break
        elif player1.score >= 5:
            print(f"{player1.name} wins with a score of {player1.score}!")
            print("Game over!")
            break

game()