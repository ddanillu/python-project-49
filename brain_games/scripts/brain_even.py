from random import randint
import prompt
from brain_games.cli import welcome_user


def play_brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer_counter = 0
    while correct_answer_counter < 3:
        random_number = randint(1, 100)
        question = f'Question: {random_number}\nYour answer: '
        answer_player = prompt.string(question).lower()
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'

        if answer_player == correct_answer:
            print('Correct!')
            correct_answer_counter += 1
        else:
            print(f"'{answer_player}' is wrong answer ;( "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            correct_answer_counter = 0 
            return
    print(f'Congratulations, {name}!')
    
    
def main():
    play_brain_even()

    if __name__ == "__main__":
        main()