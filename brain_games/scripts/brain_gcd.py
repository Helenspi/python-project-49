#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.logic import record_logic


def main():
    """
    Function runs record_logic function
    Arg: gcd module
    """
    record_logic(gcd)


if __name__ == '__main__':
    main()
