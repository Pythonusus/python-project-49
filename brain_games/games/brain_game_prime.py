"""This module provides all necessary functions for brain_prime"""

import random

import brain_games.games.common_games_operations as cgo

MIN_NUMBER = 0  # Minimal number to be used in the game
MAX_NUMBER = 100  # Maximum number to be used in the game
RULES_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for i in range(2, round((num ** 0.5)) + 1):
        if num % i == 0:
            return False
    return True


def get_correct_answer(num):
    return 'yes' if is_prime(num) else 'no'


def play_game():
    cgo.print_welcome_message()
    user_name = cgo.get_user_name()
    cgo.welcome_user(user_name)
    cgo.print_rules(RULES_TEXT)

    for _ in range(cgo.CORRECT_ANSWERS_TO_WIN):
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
