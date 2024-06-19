import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def problem():
    number = random.randint(1, 200)
    if number % 2 == 0:
        number = number + 1

    if number == 1:
        result = 'no'
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            result = 'no'
    result = 'yes'
    return number, result
