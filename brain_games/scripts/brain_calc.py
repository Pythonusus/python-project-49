#!/usr/bin/env python3
"""This script starts brain-calc game.

Brain-calc is a game, where player needs to solve arithmetic problems.
"""

from brain_games.games import brain_game_calc
from brain_games.games_engine import games_engine


def main():
    games_engine(brain_game_calc)


if __name__ == '__main__':
    main()
