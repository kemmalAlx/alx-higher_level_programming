#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = -(abs(number) % 10) if number < 1 else (abs(number) % 10)

str = f'Last digit of {number} is {lastDigit}'
if lastDigit == 0:
    print(str + ' and is 0')
elif lastDigit < 6:
    print(str + ' and is less than 6 and not 0')
elif lastDigit >= 5:
    print(str + ' and is greater than 5')
