"""This module provides all necessary functions for brain_gcd"""

import random

import brain_games.games.common_games_operations as cgo

RULES_TEXT = 'What number is missing in the progression?'
MIN_PROGRESSION_START = 0
MAX_PROGRESSION_START = 10
MIN_COMMON_DIFFERENCE = 1
MAX_COMMON_DIFFERENCE = 10
MIN_PROGRESSON_LENGTH = 5
MAX_PROGRESSON_LENGTH = 15


def generate_progression(
        min_start=0, max_start=10,
        min_diff=1, max_diff=10,
        min_len=5, max_len=15
):

    progression_start = random.randint(min_start, max_start)
    progression_common_difference = random.randint(min_diff, max_diff)
    progression_length = random.randint(min_len, max_len)

    progression = []
    current_member = progression_start
    for _ in range(progression_length):
        progression.append(current_member)
        current_member += progression_common_difference

    return progression


def get_progression_copy_with_hidden_element(progression, index):
    new_progression = progression.copy()
    new_progression[index] = '..'
    return new_progression


def play_game():
    cgo.print_welcome_message()
    user_name = cgo.get_user_name()
    cgo.welcome_user(user_name)
    cgo.print_rules(RULES_TEXT)

    for _ in range(cgo.CORRECT_ANSWERS_TO_WIN):
        progression = generate_progression(
            min_start=MIN_PROGRESSION_START, max_start=MAX_PROGRESSION_START,
            min_diff=MIN_COMMON_DIFFERENCE, max_diff=MAX_COMMON_DIFFERENCE,
            min_len=MIN_PROGRESSON_LENGTH, max_len=MAX_PROGRESSON_LENGTH
        )

        hidden_element_index = random.randrange(len(progression))

        progression_with_hidden_element = (
            get_progression_copy_with_hidden_element(
                progression,
                hidden_element_index
            )
        )

        print(cgo.get_question(*progression_with_hidden_element))

        answer = cgo.get_answer()
        correct_answer = str(progression[hidden_element_index])
        if not cgo.is_correct_answer(answer, correct_answer):
            cgo.print_lose_game_text(answer, correct_answer, user_name)
            break
        else:
            print('Correct!')
    else:
        cgo.print_win_game_text(user_name)
