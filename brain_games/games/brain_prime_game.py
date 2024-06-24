import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            k += 1
    return True if k <= 0 else False


def create_task():
    number = random.randint(2, 200)
    if is_prime(number) is True:
        result = 'yes'
    else:
        result = 'no'
    return number, result
