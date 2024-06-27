import random


TASK = 'What is the result of the expression?'


def calc(int_1, int_2, operator):
    if operator == '+':
        result = int_1 + int_2
    elif operator == '-':
        result = int_1 - int_2
    else:
        result = int_1 * int_2
    return result


def create_task():
    rand_numb1 = random.randint(15, 35)
    rand_numb2 = random.randint(0, 15)
    operator = random.choice(['+', '-', '*'])
    problem = f'{str(rand_numb1)} {operator} {str(rand_numb2)}'
    result = calc(rand_numb1, rand_numb2, operator)
    return problem, result
