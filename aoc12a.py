# -*- coding:utf-8; -*-
#
# Author:      arjuvi
#   AoC 2021 Day 12
# Created:     16.12.2021
# Copyright:   (c) arjuvi 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import pprint
from collections import defaultdict

class Graph(object):
    def __init__(self, connections):
        self._graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

# s = open('aoc12test.txt', 'r').read()
s = open('aoc12test2.txt', 'r').read()
# s = open('aoc12.txt', 'r').read()
# print(s)
print(s.replace('\n','-'))
solmut = []
[solmut.append(x) for x in s.replace('\n','-').split('-') if x not in solmut]
print(solmut)
solmuja=len(solmut)
lista = [l.split('-') for l in s.split()]
print(lista)
print([all([l.islower() for l in li])  for li in lista])
g = Graph(lista)
pretty_print = pprint.PrettyPrinter()
pretty_print.pprint(g._graph)

adj = [ [0]*solmuja for i in range(solmuja)]
# print(adj)
for k in range(solmuja+1):
    adj[solmut.index(lista[k][0])][solmut.index(lista[k][1])] = 1
    adj[solmut.index(lista[k][1])][solmut.index(lista[k][0])] = 1

# print(adj)

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in adj]))

column_sums = [sum([row[i] for row in adj]) for i in range(0,len(adj[0]))]

row_sums = [sum(row) for row in adj]

start = 'start'
polku = [start]
polut = []
stop = 'end'

def etsi(adj, start, stop, polku, polut):
    for i in range(solmuja):
        tutkittava = []
        if adj[solmut.index(start)][i] == 1:
            tutkittava = polku.copy()
            if start != stop and not (solmut[i].islower() and solmut[i] in tutkittava):
                tutkittava.append(solmut[i])
                etsi(adj, solmut[i], stop, tutkittava, polut)
            elif not (solmut[i].islower() and solmut[i] in polku):
                # if tutkittava not in polut:
                if True:
                    polut.append(tutkittava)
            else:
                print('else')
                print(i, solmut[i], tutkittava)
                print('pop')
                tutkittava.pop(-1)
                print(i, solmut[i], tutkittava)
    return polut

polut = etsi(adj, start, stop, polku, polut)
print(polut)
print(len(polut))
