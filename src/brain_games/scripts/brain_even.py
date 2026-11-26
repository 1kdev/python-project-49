from random import randint

from brain_games.cli import welcome_user, wrong_answer_message, correct_answer_message, winner_message



def main():
    name = welcome_user()
    play_game(name)


def is_even(number):
    return number % 2 == 0


def play_game(name):
    correct_answer_counts = 0
    print('Answer "yes" if the number is even, otherwise answer "no"')

    while True:
        random_number = randint(0, 100)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
        print(f"Question: {random_number}")
        ask_user = input("Your answer: ")

        if is_even(random_number):
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if ask_user.lower() == correct_answer:
            correct_answer_counts += correct_answer_message()
        else:
            wrong_answer_message(ask_user, correct_answer, name)
            return

        if correct_answer_counts == 3:
            winner_message(name)
            return


if __name__ == "__main__":
    main()