# -*- coding:utf-8; -*-
#
# Author:      arjuvi
#   AoC 2021 Day 3(a)
# Created:     03.12.2021
# Copyright:   (c) arjuvi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys


s = open('input.txt', 'r').read()
# raja = len(s.split())/2
# x = ''.join([ '0' if sum([(int(x,2) & 2**bit) >> bit for x in s.split('\n')]) < raja else '1' for bit in reversed(range(12))])
# y = ''.join([ '1' if sum([(int(x,2) & 2**bit) >> bit for x in s.split('\n')]) < raja else '0' for bit in reversed(range(12))])
# print(x,y)
# print(int(x,2),int(y,2),int(x,2)*int(y,2))
# z = ' '.join([''.join([str(b) if sum([(int(x,2) & 2**bit) >> bit for x in s.split('\n')]) < raja else str(1-b) for bit in reversed(range(12))]) for b in range(2)])
# print(z)

# Python 3.7
# from functools import reduce
# from operator import mul
# zz = reduce(mul, [int(''.join([str(b) if sum([(int(x,2) & 2**bit) >> bit for x in s.split('\n')]) < len(s.split())/2 else str(1-b) for bit in reversed(range(12))]),2) for b in range(2)], 1)
# print(zz)

# Python 3.8 -->
from math import prod
zz = prod([int(''.join([str(b) if sum([(int(x,2) & 2**bit) >> bit for x in s.split('\n')]) < len(s.split())/2 else str(1-b) for bit in reversed(range(12))]),2) for b in range(2)])
print(zz)

