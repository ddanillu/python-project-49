from secrets import choice, randbelow

from brain_games.scripts.game_responses import check_answer
from brain_games.scripts.greetings import welcome_user


def get_arithmetic_progression(start, index, step, lost_index):
    arithmetic_progression = []
    for i in range(index):
        if i == lost_index:
            arithmetic_progression.append('..')
        else:
            next_number = start + i * step
            arithmetic_progression.append(str(next_number))
    return ' '.join(arithmetic_progression) 
    

def play_brain_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    correct_answer_counter = 0
    while correct_answer_counter < 3:
        start = randbelow(20)
        step = choice(range(2, 11))
        index = choice(range(5, 11))
        lost_index = randbelow(index - 1)
        question = get_arithmetic_progression(start, index, step, lost_index)
        print(f"Question: {question}")
        correct_answer = start + lost_index * step
        user_input = input('Your answer: ')
        answer_player = int(user_input)
        if check_answer(answer_player, correct_answer, name):
            correct_answer_counter += 1
        else:
            return
    print(f'Congratulations, {name}!')

