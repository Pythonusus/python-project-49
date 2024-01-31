"""This module provides all necessary functions for brain_even"""

import random

import brain_games.common_games_operations as cgo

MIN_NUMBER = 0
MAX_NUMBER = 100


def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_random_num():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_question(num):
    question = f'Question: {num}'
    return question


def get_answer():
    answer = input('Your answer: ')
    return answer


def is_even(num):
    return num % 2 == 0


def get_correct_answer(num):
    return 'yes' if is_even(num) else 'no'


def play_game():
    user_name = cgo.get_user_name()
    cgo.welcome_user(user_name)
    print_rules()

    for _ in range(3):
        number = get_random_num()
        print(get_question(number))

        answer = get_answer()
        correct_answer = get_correct_answer(number)
        if answer != correct_answer:
            cgo.print_lose_game_text(answer, correct_answer, user_name)
            break
        else:
            print('Correct!')
    else:
        cgo.print_win_game_text(user_name)
