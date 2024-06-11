#!/usr/bin/env python3


import prompt
import random


def even_number():
    name = prompt.string('May I have your name? ')
    print("Hello," + name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index < 3:
        rand_numb = random.randint(1, 100)
        print("Question:" + str(rand_numb))
        answer = prompt.string('Your answer: ')
        if ((rand_numb % 2 == 0 and answer == 'yes') or
           (rand_numb % 2 != 0 and answer == 'no')):
            print('Correct!')
            index += 1
            if index == 3:
                print("Congratulations," + name + "!")
        else:
            if rand_numb % 2 == 0 and answer != 'yes':
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was 'yes'.\nLet's try again, {name}!")
                break
            elif rand_numb % 2 != 0 and answer != 'no':
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was 'no'.\nLet's try again, {name}!")
                break


def main():
    print('Welcome to the Brain Games!')
    even_number()


if __name__ == '__main__':
    main()
