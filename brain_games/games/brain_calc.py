from secrets import randbelow, choice

from brain_games.scripts.greetings import welcome_user
from brain_games.scripts.game_responses import check_answer


def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return max(a, b) - min(a, b)
    elif op == '*':
        return a * b

def play_brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    correct_answer_counter = 0
    calc_operations = ['+', '-', '*']
    while correct_answer_counter < 3:
        a, b = randbelow(51), randbelow(51)
        op = choice(calc_operations)
        print(f'Question: {max(a, b)} {op} {min(a, b)}')
        correct_answer = calculate(a, b, op)
        user_input = input('Your answer: ')
        answer_player = int(user_input)
        if check_answer(answer_player, correct_answer, name):
            correct_answer_counter += 1
        else:
            return
    print(f'Congratulations, {name}!')

        
