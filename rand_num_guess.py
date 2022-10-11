#!/usr/bin/env python3

# Created By: Jessah
# Date: Oct 11, 2022
# This program generates a random number and makes the user guess
# if its correct with if,then,else statements

import random


def main():

    num = int(input("Guess a number between 0 to 9: "))

    random_variable = random.randint(0, 9)

    if num == random_variable:
        print("Right!")

    else:
        print("Wrong!")


if __name__ == "__main__":
    main()
