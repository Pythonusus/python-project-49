#!/usr/bin/env python3
"""This script starts brain-progression game.

Brain-progression is a game, where player needs to find missing
number in progression.
"""

from brain_games.games import brain_game_progression
from brain_games.games.games_engine import games_engine


def main():
    games_engine(brain_game_progression)


if __name__ == '__main__':
    main()
