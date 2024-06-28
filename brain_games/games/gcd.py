import random


TASK = 'Find the greatest common divisor of given numbers.'


def find_gcd(num_1, num_2):
    """
    Function finds the greatest
    common divisor of given numbers.
    Arg: number 1, number 2
    Returns: number - the greatest common
    divisor of number 1 and number 2
    """
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    return (num_1 + num_2)


def create_task():
    """
    Function generates 2 random numbers and
    applies find_gcd function to them.
    Arg: no
    Returns: 2 numbers, number - the greatest
    common divisor of number 1 and number 2
    """
    number_1 = random.randrange(2, 200, 2)
    number_2 = random.randrange(2, 200, 2)
    problem = f'{number_1} {number_2}'
    result = find_gcd(number_1, number_2)
    return problem, result
