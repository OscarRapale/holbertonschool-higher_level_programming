#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_int = set()

    for element in my_list:
        unique_int.add(element)
        total = sum(unique_int)

    return total
