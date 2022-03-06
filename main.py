"""python exercise by Radek"""

import random

COST_OF_SINGLE_DRAW = 3
my_numbers = {8, 1, 10, 28, 26, 6}
all_possible_numbers = range(1, 50)


def draw_numbers():
    """Draw 6 lotto numbers
    Returns:
    set: collection with 6 different totek numbers from range 1 to 49
    """
    return set(random.sample(all_possible_numbers, k=6))


def play_until_you_win(numbers, drawing_numbers_algorithm):
    """Keep drawing are numbers until you win
    Args:
        bet_numbers (set): user choice numbers
        drawing_numbers_algorithm (function): algorithm for drawing numbers

        Returns:
            int: number-of_attempts to win
        """
    random_numbers = {}
    counter = 0


    while numbers != random_numbers:
        random_numbers = drawing_numbers_algorithm()
        counter += 1

    return counter

if __name__ == '__main__':
    COUNTER = play_until_you_win(my_numbers, draw_numbers)
    TOTAL_COST = COST_OF_SINGLE_DRAW * COUNTER
    print(f'koszt "inwestycji"wynosi {TOTAL_COST:,}.')
