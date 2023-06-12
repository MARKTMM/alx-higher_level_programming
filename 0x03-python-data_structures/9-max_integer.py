#!/usr/bin/python3
# finds the biggest integer of a list


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    lnum = my_list[0]
    for num in my_list:
        if lnum < num:
            lnum = num
    return lnum
