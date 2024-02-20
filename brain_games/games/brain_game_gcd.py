"""This module provides all necessary functions for brain_gcd"""

import math
import random

from brain_games.constants import MAX_NUMBER, MIN_NUMBER

RULES_TEXT = 'Find the greatest common divisor of given numbers.'


def generate_game_round():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'Question: {number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
