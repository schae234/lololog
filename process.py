#!/usr/bin/env python3

import sys
import csv

def get_best_matches(csvfile):
    """Find the best match for each transcript"""
    FIRST_ID = 0
    SECOND_ID = 1

    best = []
    prevbest = next(csvfile)

    for row in csvfile:
        if row[FIRST_ID] == row[SECOND_ID]:
            pass
        else:
            if row[FIRST_ID] != prevbest[FIRST_ID]:
                if row[FIRST_ID][0:4] != row[SECOND_ID][0:4]:
                    sys.stdout.write('\t'.join(row) + '\n')
                    best.append(row)
                    prevbest = row

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

        finally:
            sys.exit(0)

if __name__ == '__main__':
    main()
