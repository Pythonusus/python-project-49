"""This module provides functions common to all brain games"""

import prompt


def get_user_name():
    return prompt.string('May I have your name? ')


def welcome_user(user_name):
    print(f'Hello, {user_name}!')


def print_win_game_text(user_name):
    print(f'Congratulations, {user_name}!')


def print_lose_game_text(answer, correct_answer, user_name):
    print(
        f'"{answer}" is wrong answer ;(. '
        f'Correct answer was "{correct_answer}".'
    )
    print(f'Let\'s try again, {user_name}!')
