import operator
import random
from random import randint

from brain_games.cli import welcome_user


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
            correct_answers_count += 1
            print("Correct!")

        else:
            print(f"'{ask_user}' is wrong answer ;(. "
                    f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if correct_answers_count == 3:
            print(f"Congratulations, {name}!")
            return


if __name__ == "__main__":
    main()