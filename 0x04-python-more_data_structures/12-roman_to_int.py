#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    res = 0
    roman_string = roman_string.upper()
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and \
                d[roman_string[i]] < d[roman_string[i + 1]]:
            res -= d[roman_string[i]]
        else:
            res += d[roman_string[i]]

    return res
