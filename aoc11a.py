# -*- coding:utf-8; -*-
#
# Author:      arjuvi
#   AoC 2021 Day 11
# Created:     14.12.2021
# Copyright:   (c) arjuvi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
from math import floor

def tulosta(ss,n):
    print('\n'.join([ss[i:i+n] for i in range(0, len(ss), n)]))

def adj2(s, i, n, nn, offset):
    if (i % n + nn*(floor(i / nn) + offset)) % n == 0: # indeksi on vasemmassa reunassa, ei muuteta edellisen rivin arvoja (n on rivin pituus)
        return ''.join([str((int(s[j])+1) % 10) if j >= (i % n + nn*(floor(i / nn) + offset)) and j < (i % n + nn*(floor(i / nn) + offset) + 2) and s[j] != 'x' and s[j] != '0' else s[j] for j in range(len(s))])
    if ((i % n + nn*(floor(i / nn) + offset))+1) % n == 0: # indeksi on vasemmassa oikeassa, ei muuteta seuraavan rivin arvoja
        return ''.join([str((int(s[j])+1) % 10) if j >= (i % n + nn*(floor(i / nn) + offset) - 1) and j < (i % n + nn*(floor(i / nn) + offset) + 1) and s[j] != 'x' and s[j] != '0' else s[j] for j in range(len(s))])
    return ''.join([str((int(s[j])+1) % 10) if j >= (i % n + nn*(floor(i / nn) + offset) - 1) and j < (i % n + nn*(floor(i / nn) + offset) + 2) and s[j] != 'x' and s[j] != '0' else s[j] for j in range(len(s))])

def adj(s, i, n, nn):
    s = adj2(s, i, n, nn, 0)
    if i >= n: # tämä vain jos ei olla ekalla rivillä
        s = adj2(s, i, n, nn, -1)
    if i < nn*n - n: # tämä vain jos ei olla viimeisellä rivillä
        s = adj2(s, i, n, nn, 1)
    return s

def kasvata(ss, n, nn, osumia):
    nollat = [i for i in range(len(ss)) if ss[i:i+1] == '0']
    # print(nollat)
    if nollat != []:
        osumia += len(nollat)
        ss = ss.replace('0','x')
        for i in range(len(nollat)):
            ss = adj(ss, nollat[i], n, int(nn/n))
        # tulosta(ss,n)
        ss,osumia = kasvata(ss, n, nn, osumia)
    return ss.replace('x','0'),osumia


# s = open('aoc11test.txt', 'r').read()
# s = open('aoc11test2.txt', 'r').read()
s = open('aoc11.txt', 'r').read()
rivit = s.split('\n')
n=len(rivit[0])
nn=n * len(rivit)
osumia = 0

iteraatioita = 500
loyty = False
for k in range(iteraatioita):
    rivit = ''.join([str((int(c)+1) % 10) for line in rivit for c in line if int(c) >= 0])
    rivit,osumia=kasvata(rivit, n, nn, osumia)
    if k == 100:
        print('\n(a) Final - Step 100\n')
        tulosta(rivit,n)
        print('Osumia: {}'.format(osumia))
    try:
        if not loyty and int(rivit,2) == 0:
            print('\n(b) First all zero:\nStep {}'.format(k+1))
            tulosta(rivit,n)
            loyty = True
    except ValueError:
        pass