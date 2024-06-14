import random

task = 'Answer "yes" if the number is even, otherwise answer "no".'

def problem():
    problem = random.randint(1, 100)
    return problem


def result():
    if int(problem()) % 2 == 0:
        return 'yes'
    else:
        return 'no'

