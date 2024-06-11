#!/usr/bin/env python3


import prompt
import random


def calc_numbers():
    name = prompt.string('May I have your name? ')
    print("Hello," + name + "!")
    print("What is the result of the expression?")
    index = 0
    while index < 3:
        rand_numb1 = random.randint(25, 55)
        rand_numb2 = random.randint(0, 25)
        operator = random.choice(['+', '-', '*'])
        x = f'{str(rand_numb1)} {operator} {str(rand_numb2)}'
        result = eval(x)
        print(f'Question: {str(rand_numb1)} {operator} {str(rand_numb2)}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            index += 1
            if index == 3:
                print("Congratulations," + name + "!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.\nLet's try again, {name}!")
            break


def main():
    print('Welcome to the Brain Games!')
    calc_numbers()


if __name__ == '__main__':
    main()
