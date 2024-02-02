"""This module provides functions common to all brain games"""

import prompt


CORRECT_ANSWERS_TO_WIN = 3


def print_welcome_message():
    print('Welcome to the Brain Games!')


def get_user_name():
    return prompt.string('May I have your name? ')


def welcome_user(user_name):
    print(f'Hello, {user_name}!')


def print_rules(rules_text):
    print(rules_text)


def get_question(*args):
    question = 'Question: '
    for arg in args:
        question = f'{question}{arg} '
    return question


def get_answer():
    answer = input('Your answer: ')
    return answer


def is_correct_answer(answer, correct_answer):
    return answer == correct_answer


def print_win_game_text(user_name):
    print(f'Congratulations, {user_name}!')


def print_lose_game_text(answer, correct_answer, user_name):
    print(
        f'"{answer}" is wrong answer ;(. '
        f'Correct answer was "{correct_answer}".'
    )
    print(f'Let\'s try again, {user_name}!')
