"""This module provides functions common to all brain games"""

import prompt


def get_username_and_welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def get_question(*args):
    question = 'Question: '
    for arg in args:
        question = f'{question}{arg} '
    return question.strip()


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
