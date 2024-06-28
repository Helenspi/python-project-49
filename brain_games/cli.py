import prompt


def welcome_user():
    """
    Function displays the greeting and asks the name.
    Arg: no
    Returns: name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello' + ', ' + name + '!')
    return name
