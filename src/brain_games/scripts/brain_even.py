from random import randint

import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    play_game(name)


def is_even(number):
    return number % 2 == 0


def play_game(name):
    correct_answer_counts = 0
    while True:
        random_number = randint(0, 100)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
        print('Answer "yes" if the number is even, otherwise answer "no"')
        print(f"Question: {random_number}")
        ask_user = input("Your answer: ")

        if is_even(random_number):
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if ask_user.lower() == correct_answer:
            print("Correct!")
            correct_answer_counts += 1
        else:
            print(f"'{ask_user}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if correct_answer_counts == 3:
            print(f"Congratulations, {name}!")
            return


if __name__ == "__main__":
    main()