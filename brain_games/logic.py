
import prompt


def game_logic(module):
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(module.TASK)
    index = 0
    while index < 3:
        log_problem, log_result = module.problem()
        print(f'Question: {log_problem}')
        answer = prompt.string('Your answer: ')
        if answer == str(log_result):
            print('Correct!')
            index += 1
            if index == 3:
                print('Congratulations, ' + name + '!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{log_result}'."
                  f"\nLet's try again, {name}!")
            break
