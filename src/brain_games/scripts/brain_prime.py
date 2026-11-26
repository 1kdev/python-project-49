from random import randint

from brain_games.cli import (
    correct_answer_message,
    welcome_user,
    winner_message,
    wrong_answer_message,
)


def main():
    name = welcome_user()
    play_game(name)


def is_prime(number):
    for d in range(2, number + 1):
        if number % d == 0:
            break
    return d == number


def play_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers_count = 0
    while True:
        number = randint(2, 100)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
        correct_answer = is_prime(number)
        print(f"Question: {number}")
        ask_user = input("Your answer: ")

        if is_prime(number):
            correct_answer = "yes"
        else:
            correct_answer = "no"

        if ask_user.lower() == correct_answer:
            correct_answers_count += correct_answer_message()
        else:
            wrong_answer_message(ask_user, correct_answer, name)
            return

        if correct_answers_count == 3:
            winner_message(name)
            return


if __name__ == "__main__":
    main()