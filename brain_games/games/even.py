import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return True if num % 2 == 0 else False


def create_task():
    problem = random.randint(1, 100)
    if is_even(problem) is True:
        result = 'yes'
    else:
        result = 'no'
    return problem, result
