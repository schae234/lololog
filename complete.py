#!/usr/bin/env python3

import sys
import csv

"""
Find orthologs by translating a bunch of TSV crap
"""

def build_lookup_table(tsvref):
    table = {}
    for entry in tsvref:
        key, val = entry
        table[key] = val

    return table

def main():
    if len(sys.argv) != 3:
        print('Wrong number of arguments')
        print('complete.py TO_FILL COMPLETED_TABLE')
        print('Columns are zero-indexed')

    else:
        inp, refp = sys.argv[1:4]

        try:
            with open(inp, mode='r') as inf, open(refp, mode='r') as reff:
                tsvin, tsvref = (csv.reader(inf, delimiter='\t'),
                                 csv.reader(reff, delimiter='\t'))

                table = build_lookup_table(tsvref)

                for row in tsvin:
                    row = row[0:5]
                    row[4] = table[row[1]]

                    sys.stdout.write('{}\n'.format('\t'.join(row)))
                    sys.stdout.flush()

        except FileNotFoundError as err:
            print(err)
            sys.exit(1)

        except BrokenPipeError:
            sys.stderr.close()

        finally:
            sys.exit(0)


if __name__ == '__main__':
    main()
