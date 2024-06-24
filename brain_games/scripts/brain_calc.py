#!/usr/bin/env python3
from brain_games.games import brain_calc_game
from brain_games.logic import record_logic


def main():
    print('Welcome to the Brain Games!')
    record_logic(brain_calc_game)


if __name__ == '__main__':
    main()
