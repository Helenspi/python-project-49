import random


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def problem():
    number = random.randint(1, 200)
    if number % 2 == 0:
        return number + 1
    else:
        return number


def result(problem):
    if problem == 1:
        return 'no'
    for i in range(2, (problem // 2) + 1):
        if problem % i == 0:
            return 'no'
    return 'yes'
