"""This module provides functions common to all brain games"""

import prompt

from brain_games.constants import CORRECT_ANSWERS_TO_WIN


def games_engine(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.RULES_TEXT)

    for _ in range(CORRECT_ANSWERS_TO_WIN):
        question, correct_answer = game.generate_game_round()
        print(question)
        user_answer = input('Your answer: ')

        if not user_answer == correct_answer:
            print(
                f'"{user_answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            print(f'Let\'s try again, {user_name}!')
            return

        print('Correct!')

    print(f'Congratulations, {user_name}!')
