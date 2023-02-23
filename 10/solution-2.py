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
        out = []
        for l in f.readlines():
            if (cycle % 40) in {x-1, x, x+1}:
                out.append('#')
            else:
                out.append('.')
            cycle += 1

            if len(l.split()) == 2:
                _, val = l.replace('\n', '').split()
                if (cycle % 40) in {x-1, x, x+1}:
                    out.append('#')
                else:
                    out.append('.')
                cycle += 1
                x += int(val)

            if len(out) == 40 * 6:
                break

    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        for i in range(6):
            f.write(f'{"".join(out[i*40:i*40+40])}\n')

if __name__ == "__main__":
    main()
