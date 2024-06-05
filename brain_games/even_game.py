import prompt
from brain_games.cli import welcome_user as welcome_user
import random

def start_game():
    get_rules()
    right_answer_count = 0
    print(f'Question: {get_random_number}')




def is_even(number):
    return True if number % 2 == 0 else False


def get_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_random_number():
    return random.randint()