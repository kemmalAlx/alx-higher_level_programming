#!/usr/bin/python3
roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "MM": 2000,
    "MMM": 3000,
    "MMMM": 4000,
}

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    total = 0
    tmp = 0
    for r in reversed(roman_string):
        current = roman.get(r)
        if not current:
            return 0
        if current >= tmp:
            total -= current
        else:
            total += current
        tmp = current
    return abs(total)
