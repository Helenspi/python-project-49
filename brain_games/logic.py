from brain_games.games.brain_calc_game import *
from brain_games.games.brain_even_game import *
import prompt

def game_logic():
    name = prompt.string('May I have your name? ')
    print('Hello,' + name + '!')
    print(task)
    index = 0
    while index < 3:
        print(f'Question: {problem()}')
        answer = prompt.string('Your answer: ')
        if answer == str(result()):
            print('Correct!')
            index += 1
            if index == 3:
                print('Congratulations,' + name + '!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result()}'.\nLet's try again, {name}!")
            break
