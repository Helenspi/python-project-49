import prompt


def game_logic(module):
    name = prompt.string('May I have your name? ')
    print('Hello,' + name + '!')
    print(module.task)
    index = 0
    while index < 3:
        x = module.problem()
        print(f'Question: {x}')
        answer = prompt.string('Your answer: ')
        if answer == str(module.result(x)):
            print('Correct!')
            index += 1
            if index == 3:
                print('Congratulations, ' + name + '!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{module.result(x)}'."
                  f"\nLet's try again, {name}!")
            break
