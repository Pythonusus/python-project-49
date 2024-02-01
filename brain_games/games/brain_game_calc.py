"""This module provides all necessary functions for brain_calc"""

import operator
import random

import brain_games.games.common_games_operations as cgo

MIN_NUMBER = 0  # Minimal number to be used in the game
MAX_NUMBER = 100  # Maximum number to be used in the game
RULES_TEXT = 'What is the result of the expression?'

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def get_random_operator(dict):
    return random.choice(list(dict.keys()))


def get_correct_answer(num1, num2, operator):
    return str(operators[operator](num1, num2))


def play_game():
    cgo.print_welcome_message()
    user_name = cgo.get_user_name()
    cgo.welcome_user(user_name)
    cgo.print_rules(RULES_TEXT)

    for _ in range(cgo.CORRECT_ANSWERS_TO_WIN):
        number1 = cgo.get_random_int(MIN_NUMBER, MAX_NUMBER)
        number2 = cgo.get_random_int(MIN_NUMBER, MAX_NUMBER)
        operator = get_random_operator(operators)
        print(cgo.get_question(number1, operator, number2))

        answer = cgo.get_answer()
        correct_answer = get_correct_answer(number1, number2, operator)
        if not cgo.is_correct_answer(answer, correct_answer):
            cgo.print_lose_game_text(answer, correct_answer, user_name)
            break
        else:
            print('Correct!')
    else:
        cgo.print_win_game_text(user_name)
