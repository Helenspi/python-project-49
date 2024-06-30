import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """
    Function determines whether a number is
    prime or not.
    Arg: number
    Returns: boolean values
    """
    if num == 2 or num == 3:
        return True
    elif num < 2 or num % 2 == 0:
        return False
    for i in range(3, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def create_task():
    """
    Function generates random number and
    applies is_prime function to it.
    Arg: no
    Returns: number, yes/no answer
    """
    number = random.randint(1, 200)
    if is_prime(number) is True:
        result = 'yes'
    else:
        result = 'no'
    return number, result
