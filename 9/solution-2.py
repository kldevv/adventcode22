'''
Advent of Code 2022
--- Part Two ---

...
'''

import sys

def main():
    ropes = [[0, 0] for _ in range(10)]
    visited = set([(0, 0)])
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for l in f:
            direction, step  = l.replace('\n', '').split()
            step = int(step)
            for i in range(step):
                # initiate movement of the head
                if direction == 'U' or direction == 'D':
                    ropes[0] = [ropes[0][0], ropes[0][1] + (1 if direction == 'U' else -1)]
                else:
                    ropes[0] = [ropes[0][0] + (1 if direction == 'R' else -1), ropes[0][1]]
                # domino the body with the movement
                for i in range(1, 10):
                    dx = ropes[i-1][0] - ropes[i][0]
                    dy = ropes[i-1][1] - ropes[i][1]
                    # one direction move, horizontal
                    if abs(dx) == 2 and dy == 0:
                        ropes[i] = [ropes[i][0] + (1 if dx > 0 else -1), ropes[i][1]]
                    # one direction move, vertical
                    elif dx == 0 and abs(dy) == 2:
                        ropes[i] = [ropes[i][0], ropes[i][1] + (1 if dy > 0 else -1)]
                    # two direction move, diagonal
                    elif abs(dx) + abs(dy) >= 3:
                        ropes[i] = [ropes[i][0] + (1 if dx > 0 else -1), ropes[i][1] + (1 if dy > 0 else -1)]
                visited.add(tuple(ropes[9]))

    out = len(visited)
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(f'{out}\n')

if __name__ == "__main__":
    main()
