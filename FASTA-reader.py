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

#print(fasta)

print(list(fasta))
eingaben = sys.argv[2:]

for eingabe in eingaben:
    position = eingabe.find(':')

    if position >= 0:
        gesuchte_id =  eingabe[:position]
        gesuchte_positionen = eingabe[position+1:]

        split = gesuchte_positionen.split('-')
        anfang = int(split[0])
        ende = int(split[1])

        i = 0
        for buchstabe in fasta[gesuchte_id]:
              if i >= anfang and i < ende:
                  print(buchstabe, end='')
              i += 1
        print('\n', end='')

        print(fasta[gesuchte_id][anfang:ende])
    else:
        if not eingabe in fasta:
            print("FEHLER! Zu dieser ID gibt es keine Sequenz!")
        print(fasta[eingabe])