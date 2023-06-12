#!/usr/bin/python3
# Function retrives element from list likein c


def element_at(my_list, idx):
    if idx < 0:
        return (None)

    length = len(my_list)

    if idx > length - 1:
        return (None)

    return(my_list[idx])
