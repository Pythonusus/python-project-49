"""This module provides all necessary functions for brain_even"""

import random

import brain_games.games.common_games_operations as cgo
from brain_games.games.games_settings import (
    CORRECT_ANSWERS_TO_WIN,
    MAX_NUMBER,
    MIN_NUMBER,
)

RULES_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_correct_answer(num):
    return 'yes' if is_even(num) else 'no'


def play_game():
    user_name = cgo.get_username_and_welcome_user()
    print(RULES_TEXT)

    for _ in range(CORRECT_ANSWERS_TO_WIN):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        print(cgo.get_question(number))

        answer = cgo.get_answer()
        correct_answer = get_correct_answer(number)
        if not cgo.is_correct_answer(answer, correct_answer):
            cgo.print_lose_game_text(answer, correct_answer, user_name)
            break
        else:
            print('Correct!')
    else:
        cgo.print_win_game_text(user_name)
