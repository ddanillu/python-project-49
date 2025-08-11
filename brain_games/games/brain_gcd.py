from secrets import randbelow

from brain_games.scripts.greetings import welcome_user
from brain_games.scripts.game_responses import check_answer

def play_brain_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    correct_answer_counter = 0
    while correct_answer_counter < 3:
        a, b = randbelow(101), randbelow(101)
        print(f'Question: {a} {b}')
        user_input = input('Your answer: ')
        answer_player = int(user_input)
        a, b = max(a,b), min(a,b)
        if b == 0:
            correct_answer = a
        else:
            while b != 0:
                a, b = b, a % b
            correct_answer = a
        if check_answer(answer_player, correct_answer, name):
            correct_answer_counter += 1
        else:
            return
    print(f'Congratulations, {name}!')