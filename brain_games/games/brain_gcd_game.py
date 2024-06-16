import random


task = 'Find the greatest common divisor of given numbers.'


def problem():
    number_1 = random.randrange(2, 200, 2)
    number_2 = random.randrange(2, 200, 2)
    return f'{number_1} {number_2}'


def result(problem):
    x = problem.split()
    a = int(x[0])
    b = int(x[-1])
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)
