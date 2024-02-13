#!/usr/bin/env python3
"""This script starts brain-prime game.

Brain-prime is a game, where player needs to define if the given number
is prime.
"""

from brain_games.games import brain_game_prime
from brain_games.games.games_engine import games_engine


def main():
    games_engine(brain_game_prime)


if __name__ == '__main__':
    main()
