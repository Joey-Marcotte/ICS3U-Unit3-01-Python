#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: September 2019
# This adds two numbers together that the user inputs


def main():
    # this function adds two numbers together with user inputs

    # input
    first_number = int(input("Enter value of first number (integer): "))
    second_number = int(input("Enter value of second number (integer): "))

    # process
    answer = first_number + second_number

    # output
    print("")
    print("{0} + {1} = {2}".format(first_number, second_number, answer))


if __name__ == "__main__":
    main()
