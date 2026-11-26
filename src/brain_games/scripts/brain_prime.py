from random import randint

from brain_games.cli import welcome_user, correct_answer_message, wrong_answer_message, winner_message


def main():
    name = welcome_user()
    play_game(name)


def is_prime(number):
    for d in range(2, number + 1):
        if number % d == 0:
            break
    return d == number


def play_game(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    correct_answers_count = 0
    while True:
        number = randint(2, 100)
        correct_answer = is_prime(number)
        print(f"Question: {number}")
        user_ask = input("Your answer: ")

        if correct_answer:
            correct_answers_count += correct_answer_message()

        else:
            wrong_answer_message(user_ask, correct_answer, name)
            return

        if correct_answers_count == 3:
            winner_message(name)
            return


if __name__ == "__main__":
    main()