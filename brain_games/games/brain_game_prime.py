"""This module provides all necessary functions for brain_prime"""

import random

from brain_games.constants import MAX_NUMBER, MIN_NUMBER
from brain_games.games.common_games_operations import generate_question

RULES_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, round((num ** 0.5)) + 1):
        if num % i == 0:
            return False
    return True


def generate_game_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = generate_question(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
