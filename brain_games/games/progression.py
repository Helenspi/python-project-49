import random


TASK = 'What number is missing in the progression?'


def create_num_list():
    """
    Function generates list of 10 numbers and certain
    step between them in the list.
    Arg: no
    Returns: list of 10 numbers
    """
    step = random.randint(2, 13)
    number = random.randint(5, 25)
    list = []
    i = 0
    while i < 10:
        number = number + step
        list.append(number)
        i += 1
    return list


def create_task():
    """
    Function uses create_num_list function and
    excludes one number from list randomly.
    Arg: no
    Returns: list of 9 numbers, number that was
    excluded
    """
    list = create_num_list()
    i = random.randint(4, 7)
    result = list[i]
    list[i] = '..'
    string_numbers = ' '.join(map(str, list))
    return string_numbers, result
