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
    if len(sys.argv) != 2:
        print('Wrong number of arguments')
        print('analyze.py')

    else:
        inp = sys.argv[1]

        try:
            with open(inp, mode='r') as inf:
                reader = csv.reader(inf, delimiter='\t')
                stats = {
                    'entries': 0,
                    'already_known': 0,
                    'matches': 0,
                    'mismatches': 0,
                    'new_finds': 0,
                    'still_unknown': 0,
                }

                for row in reader:
                    stats['entries'] += 1

                    if row[0]:
                        stats['already_known'] += 1
                        if row[4]:
                            if row[0] == row[4]:
                                stats['matches'] += 1
                            else:
                                stats['mismatches'] += 1

                    if not row[0] and row[4]:
                        stats['new_finds'] += 1

                    if not row[0] and not row[4]:
                        stats['still_unknown'] += 1

                sys.stdout.write('Summary:\n')
                sys.stdout.write('--------\n')

                fmtstr = """
                Total entries: {entries}
                Already known: {already_known}
                Matching orthologs: {matches}
                Mismatches: {mismatches}
                Newly found orthologs: {new_finds}
                Still without known orthologs: {still_unknown}
                \n"""
                sys.stdout.write(fmtstr.format(**stats))

        except FileNotFoundError as err:
            print(err)
            sys.exit(1)

        except BrokenPipeError:
            sys.stderr.close()

        finally:
            sys.exit(0)


if __name__ == '__main__':
    main()
