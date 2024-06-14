import random

task = 'What is the result of the expression?'

def problem():
    rand_numb1 = random.randint(25, 55)
    rand_numb2 = random.randint(0, 25)
    operator = random.choice(['+', '-', '*'])
    problem = f'{str(rand_numb1)} {operator} {str(rand_numb2)}'
    return problem


def result():
    result = eval(problem)
    return result
