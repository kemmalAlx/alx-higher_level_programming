#!/usr/bin/python3
roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(roman_string):
    total = 0
    tmp = 0
    if type(roman_string) is str and roman_string:
        for r in reversed(roman_string):
            current = roman.get(r)
            if not current:
                return 0
            if current < tmp:
                total -= current
            else:
                total += current
            tmp = current
        return total
    return 0
