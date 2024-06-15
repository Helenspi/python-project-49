#!/usr/bin/env python3


import brain_games.games.brain_even_game
import brain_games.logic


def main():
    print('Welcome to the Brain Games!')
    brain_games.logic.game_logic(brain_games.games.brain_even_game)


if __name__ == '__main__':
    main()
