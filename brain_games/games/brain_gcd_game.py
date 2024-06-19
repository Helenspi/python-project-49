import random


TASK = 'Find the greatest common divisor of given numbers.'


def problem():
    number_1 = random.randrange(2, 200, 2)
    number_2 = random.randrange(2, 200, 2)
    problem = f'{number_1} {number_2}'
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    return problem, (number_1 + number_2)
