import prompt
import random


def start_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    get_rules(name)
    right_answer_count = 0
    while right_answer_count < 3:
        random_number = get_random_number(1, 100)
        get_question(random_number)
        user_answer = prompt.string('Your answer: ')
        if is_answer_right(user_answer, random_number):
            print('Correct!')
            right_answer_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{is_even(random_number)}'.\nLet's try again, {name}!")
            break
    if right_answer_count == 3:
        print(f'Congratulations, {name}')


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def get_rules(name):
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_random_number(a, b):
    return random.randint(a, b)


def get_question(with_number):
    print(f'Question: {with_number}')


def is_answer_right(answer, number_to_check):
    if answer.lower() == is_even(number_to_check):
        return True
    return False
