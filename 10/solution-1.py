'''
Advent of Code 2022
--- Part Two ---

...
'''

import sys

def main():
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        x = 1
        cycle = 0
        cycle_mark = [20, 60, 100, 140, 180, 220]
        cycle_mark_idx = 0
        out = 0
        for l in f.readlines():
            cycle += 1
            val = 0
            if len(l.split()) == 2:
                _, val = l.replace('\n', '').split()
                val = int(val)
                cycle += 1
            if cycle_mark_idx < len(cycle_mark) and cycle >= cycle_mark[cycle_mark_idx]:
                out += cycle_mark[cycle_mark_idx] * x
                cycle_mark_idx += 1
            x += val

    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(f'{out}\n')

if __name__ == "__main__":
    main()
