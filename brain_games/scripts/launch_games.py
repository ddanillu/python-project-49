import sys
from brain_games.games.brain_calc import play_brain_calc
from brain_games.games.brain_even import play_brain_even
from brain_games.games.brain_gcd import play_brain_gcd

def main_calc():
    play_brain_calc()

def main_even():
    play_brain_even()

def main_gcd():
    play_brain_gcd()

if __name__ == "__main__":
    game_name = sys.argv[1]
    match game_name:
        case "brain_calc":
            main_calc()
        case "brain_even":
            main_even()
        case "brain_gcd":
            main_gcd()
        case _:
            print(f"The game '{game_name}' was not found.")