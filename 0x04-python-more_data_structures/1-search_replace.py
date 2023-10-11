#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = list(map(lambda c: replace if c == search else c, my_list))
    return (my_list)
