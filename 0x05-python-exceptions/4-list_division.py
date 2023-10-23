#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for v in range(list_length):
        try:
            divli = 0
            try:
                divli = my_list_1[v] / my_list_2[v]
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
            new_list.append(divli)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
    return new_list
