'''
Advent of Code 2022
--- Part Two ---

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
'''

import sys

def main():
    out = [0] * 3
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        calories = 0
        for line in f.readlines() + ['\n']:
            line = line.replace('\n', '')
            if not line:
                if calories > out[0]:
                    out[0], out[1], out[2] = calories, out[0], out[1]
                elif calories > out[1]:
                    out[1], out[2] = calories, out[1]
                elif calories > out[2]:
                    out[2] = calories
                calories = 0
            else:
                calories += int(line)
                
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(f'{sum(out)}\n')

if __name__ == "__main__":
    main()