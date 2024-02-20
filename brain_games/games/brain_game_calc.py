"""This module provides all necessary functions for brain_calc"""

import operator
import random

from brain_games.constants import MAX_NUMBER, MIN_NUMBER

RULES_TEXT = 'What is the result of the expression?'

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def generate_game_round():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(list(operators.keys()))
    question = f'Question: {number1} {operator} {number2}'
    correct_answer = str(operators[operator](number1, number2))
    return question, correct_answer
