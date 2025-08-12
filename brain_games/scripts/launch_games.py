import sys

from brain_games.games.brain_calc import play_brain_calc
from brain_games.games.brain_even import play_brain_even
from brain_games.games.brain_gcd import play_brain_gcd
from brain_games.games.brain_prime import play_brain_prime
from brain_games.games.brain_progression import play_brain_progression


def main_calc():
    play_brain_calc()


def main_even():
    play_brain_even()


def main_gcd():
    play_brain_gcd()


def main_progression():
    play_brain_progression()


def main_prime():
    play_brain_prime()


if __name__ == "__main__":
    game_name = sys.argv[1]
    match game_name:
        case "brain_calc":
            main_calc()
        case "brain_even":
            main_even()
        case "brain_gcd":
            main_gcd()
        case "brain_progression":
            main_progression()
        case "brain_prime":
            main_prime()
        case _:
            print(f"The game '{game_name}' was not found.")