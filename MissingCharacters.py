#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

#

def missingCharacters(s):
    all_digits = set('0123456789')
    all_letters = set('abcdefghijklmnopqrstuvwxyz')

    present_digits = set([char for char in s if char.isdigit()])
    present_letters = set([char for char in s if char.isalpha()])

    missing_digits = sorted(all_digits - present_digits)
    missing_letters = sorted(all_letters - present_letters)

    return ''.join(missing_digits + missing_letters)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
