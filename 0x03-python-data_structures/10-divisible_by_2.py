#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None

    list2divs = []
    for i in my_list:
        if (i % 2) == 0:
            list2divs.append(True)
        else:
            list2divs.append(False)
    return list2divs
