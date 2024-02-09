"""This module provides all necessary functions for brain_gcd"""

import math
import random

import brain_games.games.common_games_operations as cgo
from brain_games.games.games_settings import (
    CORRECT_ANSWERS_TO_WIN,
    MAX_NUMBER,
    MIN_NUMBER,
)

RULES_TEXT = 'Find the greatest common divisor of given numbers.'


def get_correct_answer(num1, num2):
    return str(math.gcd(num1, num2))


def play_game():
    user_name = cgo.get_username_and_welcome_user()
    print(RULES_TEXT)

    for _ in range(CORRECT_ANSWERS_TO_WIN):
        number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        print(cgo.get_question(number1, number2))

        answer = cgo.get_answer()
        correct_answer = get_correct_answer(number1, number2)

        if not cgo.is_correct_answer(answer, correct_answer):
            cgo.print_lose_game_text(answer, correct_answer, user_name)
            break
        print('Correct!')

    else:
        cgo.print_win_game_text(user_name)
