import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def wrong_answer_message(ask_user: str, correct_answer: int | str | bool, name: str):
    print(f"'{ask_user}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")

def correct_answer_message():
    print("Correct!")
    return 1

def winner_message(name):
    print(f"Congratulations, {name}!")