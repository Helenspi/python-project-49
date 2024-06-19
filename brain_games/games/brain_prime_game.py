import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def problem():
    number = random.randint(1, 200)
    k = 0
    if number == 1:
        result = 'no'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k += 1
    if k <= 0:
        result = 'yes'
    else:
        result = 'no'
    return number, result
