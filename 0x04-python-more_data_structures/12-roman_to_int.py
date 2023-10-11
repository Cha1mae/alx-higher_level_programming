#!/usr/bin/python3
def subtract_smaller(list_num):
    total_to_subtract = 0
    max_in_list = max(list_num)
    for num in list_num:
        if max_in_list > num:
            total_to_subtract += num
    return (max_in_list - total_to_subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)
    roman_numerals = {'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_keys = list(roman_numerals.keys())
    result = 0
    pre_value = 0
    cur_values = [0]
    for char in roman_string:
        for numeral in numeral_keys:
            if numeral == char:
                if roman_numerals.get(char) <= pre_value:
                    result += subtract_smaller(cur_values)
                    cur_values = [roman_numerals.get(char)]
                else:
                    cur_values.append(roman_numerals.get(char))

                pre_value = roman_numerals.get(char)
    result += subtract_smaller(cur_values)
    return (result)
