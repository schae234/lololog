#!/usr/bin/env python3

import sys
import csv

def get_best_matches(csvfile):
    FIRST_ID = 0
    SECOND_ID = 1
    SCORE = 7

    best = []
    prevbestid = ''

    for row in csvfile:
        if row[FIRST_ID] == row[SECOND_ID]:
            pass
        else:
            if row[FIRST_ID] != prevbestid:
                sys.stdout.write('\t'.join(row))
                best.append(row)
                prevbestid = row[FIRST_ID]

def main():
    if len(sys.argv) != 2:
        print('Wrong number of arguments')
    else:
        filename = sys.argv[1]

        bests = []

        try:
            with open(filename) as csvin:
                csvfile = csv.reader(csvin, delimiter='\t')
                bests = get_best_matches(csvfile)

        except OSError:
            print('Could not open file {}'.format(filename))

if __name__ == '__main__':
    main()
