"""This module provides all necessary functions for brain_even"""

import random

from brain_games.constants import MAX_NUMBER, MIN_NUMBER
from brain_games.games.common_games_operations import generate_question

RULES_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def generate_game_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = generate_question(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
