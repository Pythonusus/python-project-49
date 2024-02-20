"""This module provides all necessary functions for brain_gcd"""

import math
import random

from brain_games.constants import MAX_NUMBER, MIN_NUMBER
from brain_games.games.common_games_operations import generate_question

RULES_TEXT = 'Find the greatest common divisor of given numbers.'


def get_correct_answer(num1, num2):
    return str(math.gcd(num1, num2))


def generate_game_round():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = generate_question(number1, number2)
    correct_answer = get_correct_answer(number1, number2)
    return question, correct_answer
