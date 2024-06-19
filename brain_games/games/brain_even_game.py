import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def problem():
    problem = random.randint(1, 100)
    if problem % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return problem, result
