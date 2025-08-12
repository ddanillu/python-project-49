from secrets import randbelow

from brain_games.scripts.game_responses import check_answer
from brain_games.scripts.greetings import welcome_user


def is_prime(number):
    if number <= 1:
        return 'no'
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def play_brain_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answer_counter = 0
    while correct_answer_counter < 3:
        random_number = randbelow(3572)
        print(f'Question: {random_number}')
        correct_answer = is_prime(random_number)
        answer_player = input('Your answer: ').lower()
        if check_answer(answer_player, correct_answer, name):
            correct_answer_counter += 1
        else:
            return
    print(f'Congratulations, {name}!')

