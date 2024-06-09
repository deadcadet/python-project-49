import random
import prompt


# Common functions:
def play_game(game_type):
    name = welcome_user()
    right_answer_count = 0
    get_rules(game_type)
    input_functions = {
        'even': prompt.string,
        'calc': prompt.integer
    }
    input_func = input_functions.get(game_type)
    while right_answer_count < 3:
        correct_answer = get_question(game_type)
        user_answer = input_func('Your answer: ')
        if is_answer_right(user_answer, correct_answer):
            right_answer_count += 1
        else:
            game_over(user_answer, correct_answer, name)
            break
    if right_answer_count == 3:
        game_win(name)


def get_question(game_type):
    if game_type == 'calc':
        expression, correct_answer = generate_random_expression()
        print(f"Question: {expression}")
    if game_type == 'even':
        random_number = get_random_number(1, 100)
        print(f"Question: {random_number}")
        correct_answer = 'yes' if is_even(random_number) else 'no'
    return correct_answer


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_rules(game_type):
    games = {
        'even': 'Answer "yes" if the number is even, otherwise answer "no".',
        'calc': 'What is the result of the expression?'
    }
    print(games[game_type])


def is_answer_right(usr_answer, right_answer):
    if usr_answer == right_answer:
        print('Correct!')
        return True
    return False


def game_over(usr_ans, right_ans, name):
    print(f"'{usr_ans}' is wrong answer ;(. Correct answer was '{right_ans}'.")
    print(f"Let's try again, {name}!")


def game_win(name):
    print(f'Congratulations, {name}!')


def get_random_number(a, b):
    return random.randint(a, b)


# Functions for CALC game:
def generate_random_expression():
    operators = ['+', '-', '*']
    num1 = get_random_number(1, 10)
    num2 = get_random_number(1, 10)
    operator = random.choice(operators)
    expression = f"{num1} {operator} {num2}"
    result = eval(expression)
    return expression, result


# Functions for EVEN game:
def is_even(number):
    return True if number % 2 == 0 else False
