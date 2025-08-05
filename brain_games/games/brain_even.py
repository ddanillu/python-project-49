from secrets import randbelow

import prompt

from brain_games.scripts.greetings import welcome_user
from brain_games.scripts.game_responses import check_answer


def play_brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer_counter = 0
    while correct_answer_counter < 3:
        random_number = randbelow(1001)
        question = f'Question: {random_number}\nYour answer: '
        answer_player = prompt.string(question).lower()
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        if check_answer(answer_player, correct_answer, name):
            correct_answer_counter += 1
        else:
            return
    print(f'Congratulations, {name}!')
    
    
def main():
    play_brain_even()

    if __name__ == "__main__":
        main()