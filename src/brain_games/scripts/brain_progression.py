from random import randint

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    play_game(name)


def elements_list():
    start = randint(0, 20)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    step = randint(0, 10)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    hidden_index = randint(0, 9)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    elements = []
    correct_answer = 0

    for index in range(0, 10):
        if index == hidden_index:
            elements.append("..")
            correct_answer += start + index * step
        else:
            current_element = start + index * step
            elements.append(current_element)
    return elements, correct_answer


def play_game(name):
    print("What number is missing in the progression?")
    correct_answer_counts = 0

    while True:
        numbers, correct_answer = elements_list()
        elements = " ".join(map(str, numbers))
        print(f"Question: {elements}")
        ask_user = input("Your answer: ")

        if int(ask_user) == correct_answer:
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