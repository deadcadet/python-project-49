from brain_games.cli import welcome_user as welcome_user
from brain_games.even_game import start_game as start_game
import prompt

def main():
    welcome_user()
    start_game()

if __name__ == '__main__':
    main()