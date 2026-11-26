from random import randint

from brain_games.cli import welcome_user, wrong_answer_message, correct_answer_message, winner_message


def main():
    name = welcome_user()
    play_game(name)


def gcd_calc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def play_game(name):
    print("Find the greatest common divisor of given numbers.")
    correct_answers_count = 0
    while True:
        a, b = randint(0, 100), randint(0, 100)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
        correct_answer = gcd_calc(a, b)
        print(f"Question: {a} {b}")
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