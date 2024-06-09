from brain_games.scripts.game_functions import play_game as play_game
from brain_games.scripts.game_functions import get_question_even as get_question_even  # noqa E501


def main():
    play_game('even', get_question_even)


if __name__ == '__main__':
    main()
