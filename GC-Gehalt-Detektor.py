#!/bin/python

import sys

print(sys.argv)
filename = sys.argv[1]

fasta = {}

id = ''

for zeile in open(filename):
    #zeile = zeile.strip()
    zeile = zeile[:len(zeile)-1]

    if zeile.startswith('>'):
        id = zeile[1:]
        fasta[id] = ''
    else:
        #print(id)
        #print(zeile)
        fasta[id] += zeile

print(fasta)