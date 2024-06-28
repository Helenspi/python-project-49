#!/usr/bin/env python3
from brain_games.games import calc
from brain_games.logic import record_logic


def main():
    """
    Function runs record_logic function
    Arg: calc module
    """
    record_logic(calc)


if __name__ == '__main__':
    main()
