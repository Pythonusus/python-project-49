#!/usr/bin/env python3
"""This script starts brain-even game.

Brain-even is a game, where player needs to define if number is even.
"""

from brain_games.games import brain_game_even
from brain_games.games_engine import games_engine


def main():
    games_engine(brain_game_even)


if __name__ == '__main__':
    main()
