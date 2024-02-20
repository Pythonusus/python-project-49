"""This module provides all necessary functions for brain_gcd"""

import random

RULES_TEXT = 'What number is missing in the progression?'
MIN_PROGRESSION_START = 0
MAX_PROGRESSION_START = 10
MIN_COMMON_DIFFERENCE = 1
MAX_COMMON_DIFFERENCE = 10
MIN_PROGRESSON_LENGTH = 5
MAX_PROGRESSON_LENGTH = 15


def generate_progression(start=0, common_diff=1, length=10):
    progression = []
    current_member = start
    for _ in range(length):
        progression.append(current_member)
        current_member += common_diff

    return progression


def get_progression_copy_with_hidden_element(progression, index):
    new_progression = progression.copy()
    new_progression[index] = '..'
    return new_progression


def generate_question(*args):
    question = 'Question: '
    for arg in args:
        question = f'{question}{arg} '
    return question.strip()


def generate_game_round():
    progression_start = random.randint(
        MIN_PROGRESSION_START,
        MAX_PROGRESSION_START
    )

    progression_common_difference = random.randint(
        MIN_COMMON_DIFFERENCE,
        MAX_COMMON_DIFFERENCE
    )

    progression_length = random.randint(
        MIN_PROGRESSON_LENGTH,
        MAX_PROGRESSON_LENGTH
    )

    progression = generate_progression(
        progression_start,
        progression_common_difference,
        progression_length
    )

    hidden_element_index = random.randrange(len(progression))

    progression_with_hidden_element = (
        get_progression_copy_with_hidden_element(
            progression,
            hidden_element_index
        )
    )

    question = generate_question(*progression_with_hidden_element)
    correct_answer = str(progression[hidden_element_index])

    return question, correct_answer
