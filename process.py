#!/usr/bin/env python3

import sys
import csv

def get_best_matches(csvfile):
    """"""
    FIRST_ID = 0
    SECOND_ID = 1

    best = []
    prevbestid = ''

    for row in csvfile:
        if row[FIRST_ID] == row[SECOND_ID]:
            pass
        else:
            if row[FIRST_ID] != prevbestid:
                sys.stdout.write('\t'.join(row) + '\n')
                best.append(row)
                prevbestid = row[FIRST_ID]

    return best

def main():
    """Main method"""
    if len(sys.argv) != 2:
        print('Wrong number of arguments')
    else:
        filename = sys.argv[1]

        bests = []

        try:
            with open(filename) as csvin:
                csvfile = csv.reader(csvin, delimiter='\t')
                bests = get_best_matches(csvfile)

        except FileNotFoundError:
            print('Could not open file {}'.format(filename))

        except BrokenPipeError:
            sys.stderr.close()
            sys.exit(0)

        finally:
            sys.exit(0)

if __name__ == '__main__':
    main()
