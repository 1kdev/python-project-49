import operator
import random
from random import randint

from brain_games.cli import welcome_user, wrong_answer_message, winner_message, correct_answer_message


def main():
    name = welcome_user()
    play_game(name)


def play_game(name):
    correct_answers_count = 0
    action = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    math_sign = random.choice(list(action))  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    print("What is the result of the expression?")

    while True:
        first_num, second_num = randint(0, 30), randint(0, 25)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
        correct_answer = action[math_sign](first_num, second_num)
        print(f"Question: {first_num} {math_sign} {second_num}")
        ask_user = input("Your answer: ")

        if int(ask_user) == correct_answer:
            correct_answers_count += correct_answer_message()

        else:
            wrong_answer_message(ask_user, correct_answer, name)
            return

        if correct_answers_count == 3:
            winner_message(name)
            return


if __name__ == "__main__":
    main()