'''
Advent of Code 2022
--- Part Two ---

Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

  30373
  25512
  65332
  33549
  35390

Looking up, its view is not blocked; it can see 1 tree (of height 3).
Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
Looking right, its view is not blocked; it can see 2 trees.
Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

  30373
  25512
  65332
  33549
  35390

Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
Looking left, its view is not blocked; it can see 2 trees.
Looking down, its view is also not blocked; it can see 1 tree.
Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?
'''

import sys
from collections import defaultdict

def main():
    trees = []
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for l in f:
            trees.append(list(map(int, l.replace('\n', ''))))

    n = len(trees)
    m = len(trees[0]) if trees else 0
    
    scores = [[1]* m for _ in range(n)]

    col_stk = [[] for _ in range(m)]
    for i in range(n):
        row_stk = []
        for j in range(m):
            while row_stk and trees[i][j] > trees[i][row_stk[-1]]:
                row_stk.pop()
            while col_stk[j] and trees[i][j] > trees[col_stk[j][-1]][j]:
                col_stk[j].pop()
            scores[i][j] *= abs(j - (row_stk[-1] if row_stk else 0))
            scores[i][j] *= abs(i - (col_stk[j][-1] if col_stk[j] else 0))
            row_stk.append(j)
            col_stk[j].append(i)
    
    out = 0

    col_stk = [[] for _ in range(m)]
    for i in range(n-1, -1, -1):
        row_stk = []
        for j in range(m-1, -1, -1):
            while row_stk and trees[i][j] > trees[i][row_stk[-1]]:
                row_stk.pop()
            while col_stk[j] and trees[i][j] > trees[col_stk[j][-1]][j]:
                col_stk[j].pop()
            scores[i][j] *= abs(j - (row_stk[-1] if row_stk else m - 1))
            scores[i][j] *= abs(i - (col_stk[j][-1] if col_stk[j] else n - 1))
            out = max(out, scores[i][j])
            row_stk.append(j)
            col_stk[j].append(i)

    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(f'{out}\n')

if __name__ == "__main__":
    main()