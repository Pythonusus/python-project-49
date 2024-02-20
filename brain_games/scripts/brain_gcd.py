#!/usr/bin/env python3
"""This script starts brain-gcd game.

Brain-gcd is a game, where player needs to find greatest common devisor.
"""

from brain_games.games import brain_game_gcd
from brain_games.games_engine import games_engine


def main():
    games_engine(brain_game_gcd)


if __name__ == '__main__':
    main()
