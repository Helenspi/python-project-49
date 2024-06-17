import random


task = 'What number is missing in the progression?'


def numbers_list():
    step = random.randint(2, 13)
    number = random.randint(5, 25)
    list = []
    i = 0
    while i < 10:
        number = number + step
        list.append(number)
        i += 1
    return list


def problem():
    list = numbers_list()
    i = random.randint(4, 7)
    list[i] = '..'
    string_numbers = ' '.join(map(str, list))
    return string_numbers


def result(problem):
    result_list = problem.split()
    i = result_list.index('..')
    result = (int(result_list[i + 1]) + int(result_list[i - 1])) // 2
    return result
