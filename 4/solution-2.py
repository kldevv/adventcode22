'''
Advent of Code 2022
--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
'''

import sys

def main():
    out = 0
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for line in f.readlines():
            (e1_start, e1_end), (e2_start, e2_end) = map(lambda x: map(int, x.split('-')), line.split(','))
            # merge interval
            if not (e2_end < e1_start or e1_end < e2_start):    
                out += 1
                
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(f'{out}\n')

if __name__ == "__main__":
    main()