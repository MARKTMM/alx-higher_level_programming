#!/usr/bin/python3
# Replaces the element at the specified index in list with specified element

def new_in_list(my_list, idx, element):
    length = len(my_list)

    copy_list = my_list[:]

    if 0 <= idx < length:
        copy_list[idx] = element

    return(copy_list)
