#!/usr/bin/python3

for firt_digit in range(0, 10):
    for second_digit in range(firt_digit + 1, 10):

        if firt_digit == 8 and second_digit == 9:
            print("{}{}".format(firt_digit, second_digit))

        else:
            print("{}{}".format(firt_digit, second_digit), end=", ")
