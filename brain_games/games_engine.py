"""This module provides functions common to all brain games"""

import prompt
from brain_games.games.games_settings import CORRECT_ANSWERS_TO_WIN


def get_username():
    user_name = prompt.string('May I have your name? ')
    return user_name


def welcome_user(user_name):
    print(f'Hello, {user_name}!')


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


def games_engine(game):
    print('Welcome to the Brain Games!')
    user_name = get_username()
    welcome_user(user_name)
    print(game.RULES_TEXT)

    for _ in range(CORRECT_ANSWERS_TO_WIN):
        question, correct_answer = game.generate_game_round()
        print(question)
        answer = get_answer()

        if not is_correct_answer(answer, correct_answer):
            print_lose_game_text(answer, correct_answer, user_name)
            return

        print('Correct!')

    print_win_game_text(user_name)
