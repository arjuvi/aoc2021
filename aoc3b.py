# -*- coding:utf-8; -*-
#
# Author:      arjuvi
#   AoC 2021 Day 3(b)
# Created:     09.12.2021
# Copyright:   (c) arjuvi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def xnor(a,b):
    return a and b or not a and not b

def removeItems(lst, i, b):
    # print(lst)
    someCommon = ''.join([str(b) if sum([(int(x,2) & 2**bit) >> bit for x in lst]) < len(lst)/2 else str(1-b) for bit in reversed(range(i))])
    if i > 0 and len(lst) > 1:
        return removeItems([binnum for binnum in lst for bit in reversed(range(i-1,i)) if (xnor(((int(binnum,2) & 2**bit) >> bit),(int(someCommon,2) & 2**bit) >> bit))], i-1, b)
    return lst

s = open('aoc3.txt', 'r').read()
# s = open('aoc3Test.txt', 'r').read()
d = s.split('\n')
pituus = len(d[0])
print(int(removeItems(d, pituus, 0)[0],2) * int(removeItems(d, pituus, 1)[0],2))
