def check_answer(answer_player, correct_answer, name):
    if answer_player == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer_player}' is wrong answer ;( "
            f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False