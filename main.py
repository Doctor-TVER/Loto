from lotoshka import *


game = Game()
while True:
    score = game.play_round()
    if score == 1:
        print('You win')
        break
    elif score == 2:
        print('You lose')
        break
