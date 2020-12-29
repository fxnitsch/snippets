# -*- coding: utf-8 -*-

import os
import random


def clear():
    os.system("clear")


def create_code(digits):
    """ Returns list of random integer values for number of `digits` provided """
    return [random.randint(1, 6) for _ in range(0, digits)]


def get_guess(digits):
    """ Returns user input as list of integers after checking for correct number of `digits` """
    guess = list()
    while len(guess) != digits:
        try:
            guess = [int(item) for item in input("Enter your guess consisting of {} digits: ".format(digits)).split()]
        except ValueError:
            print("Please only enter {} integer values separated by a space.".format(digits))
    return guess


def compare_input(guess, code, flags):
    """ Checks user guess and returns flags """
    for position, i in enumerate(code):
        if guess[position] == i:
            flags[position] = "X"
        elif i in guess:
            flags[position] = "0"
        else:
            flags[position] = "-"
    return sorted(flags)


def check_for_win(flags):
    """ Returns true if all flags are set to 'X' """
    if all(i == "X" for i in flags):
        return True
    else:
        return False


def run():
    turn = 1
    chances = 6
    digits = 4
    code = create_code(digits)
    flags = ['-'] * digits
    print("Guess the {} digit code with values between 1 and 6. "
          "You may only use a maximum of {} guesses. \n".format(digits, chances))
    while turn <= chances:
        guess = get_guess(digits)
        flags = compare_input(guess, code, flags)
        if check_for_win(flags):
            print("You solved it in {} turns! Congratulations, master mind.".format(turn))
            quit()
        else:
            print(" Turn {}:".format(turn), flags, "\n")
            turn += 1
    print("You ran out of guesses. \n The code is {}".format(code))


if __name__ == '__main__':
    run()
