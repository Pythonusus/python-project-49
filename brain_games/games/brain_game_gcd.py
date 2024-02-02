"""This module provides all necessary functions for brain_gcd"""

import math

import brain_games.games.common_games_operations as cgo

MIN_NUMBER = 0  # Minimal number to be used in the game
MAX_NUMBER = 100  # Maximum number to be used in the game
RULES_TEXT = 'Find the greatest common divisor of given numbers.'


def get_correct_answer(num1, num2):
    return str(math.gcd(num1, num2))


def play_game():
    cgo.print_welcome_message()
    user_name = cgo.get_user_name()
    cgo.welcome_user(user_name)
    cgo.print_rules(RULES_TEXT)

    for _ in range(cgo.CORRECT_ANSWERS_TO_WIN):
        number1 = cgo.get_random_int(MIN_NUMBER, MAX_NUMBER)
        number2 = cgo.get_random_int(MIN_NUMBER, MAX_NUMBER)
        print(cgo.get_question(number1, number2))

        answer = cgo.get_answer()
        correct_answer = get_correct_answer(number1, number2)
        if not cgo.is_correct_answer(answer, correct_answer):
            cgo.print_lose_game_text(answer, correct_answer, user_name)
            break
        else:
            print('Correct!')
    else:
        cgo.print_win_game_text(user_name)
