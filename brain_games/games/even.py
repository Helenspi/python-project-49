import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """
    Function determines whether a number is
    even or not.
    Arg: number
    Returns: boolean values
    """
    return True if num % 2 == 0 else False


def create_task():
    """
    Function generates random number and
    applies is_even function to it.
    Arg: no
    Returns: number, yes/no answer
    """
    problem = random.randint(1, 100)
    if is_even(problem) is True:
        result = 'yes'
    else:
        result = 'no'
    return problem, result
