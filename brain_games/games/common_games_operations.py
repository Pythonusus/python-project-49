"""This module provides functions common to all brain games"""


def generate_question(*args):
    question = 'Question: '
    for arg in args:
        question = f'{question}{arg} '
    return question.strip()
