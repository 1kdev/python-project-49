from random import randint

from brain_games.cli import welcome_user


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
        gcd = gcd_calc(a, b)
        print(f"Question: {a} {b}")
        ask_user = input("Your answer: ")

        if int(ask_user) == gcd:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{ask_user}' is wrong answer ;(. "
                    f"Correct answer was '{gcd}'")
            print(f"Let's try again, {name}!")
            return

        if correct_answers_count == 3:
            print(f"Congratulations, {name}!")
            return


if __name__ == "__main__":
    main()