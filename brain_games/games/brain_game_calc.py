"""This module provides all necessary functions for brain_calc"""

import operator
import random

from brain_games.games.common_games_operations import generate_question
from brain_games.games.games_settings import MAX_NUMBER, MIN_NUMBER

RULES_TEXT = 'What is the result of the expression?'

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def get_random_operator(dict):
    return random.choice(list(dict.keys()))


def get_correct_answer(num1, num2, operator):
    return str(operators[operator](num1, num2))


def generate_game_round():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = get_random_operator(operators)
    question = generate_question(number1, operator, number2)
    correct_answer = get_correct_answer(number1, number2, operator)
    return question, correct_answer
