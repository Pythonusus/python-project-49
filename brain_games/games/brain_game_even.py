"""This module provides all necessary functions for brain_even"""

import random

from brain_games.games.common_games_operations import generate_question
from brain_games.games.games_settings import MAX_NUMBER, MIN_NUMBER

RULES_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_correct_answer(num):
    return 'yes' if is_even(num) else 'no'


def generate_game_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = generate_question(number)
    correct_answer = get_correct_answer(number)
    return question, correct_answer
