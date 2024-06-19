

import random


TASK = 'What is the result of the expression?'


def problem():
    rand_numb1 = random.randint(15, 35)
    rand_numb2 = random.randint(0, 15)
    operator = random.choice(['+', '-', '*'])
    problem = f'{str(rand_numb1)} {operator} {str(rand_numb2)}'
    if operator == '+':
        result = rand_numb1 + rand_numb2
    elif operator == '-':
        result = rand_numb1 - rand_numb2
    else:
        result = rand_numb1 * rand_numb2
    return problem, result
