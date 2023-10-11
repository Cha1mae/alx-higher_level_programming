#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    d_num = 0

    for j in uniq_list:
        d_num += j

    return (d_num)
