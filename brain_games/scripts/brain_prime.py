#!/usr/bin/env python3


from brain_games.games import brain_prime_game
from brain_games.logic import game_logic


def main():
    print('Welcome to the Brain Games!')
    game_logic(brain_prime_game)


if __name__ == '__main__':
    main()
