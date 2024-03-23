#!/usr/bin/python3

if __name__ == "__main__":
    """This program prints the result of the addition of all arguments"""

from sys import argv

len = len(argv) - 1
sum = 0
for i in range(1, len + 1):
    sum += int(argv[i])
print(sum)
