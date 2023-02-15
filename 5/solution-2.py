'''
Advent of Code 2022
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

      [D]    
  [N] [C]    
  [Z] [M] [P]
  1   2   3 

Moving a single crate from stack 2 to stack 1 behaves the same as before:

  [D]        
  [N] [C]    
  [Z] [M] [P]
  1   2   3 

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

          [D]
          [N]
      [C] [Z]
      [M] [P]
  1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

          [D]
          [N]
  [C]     [Z]
  [M]     [P]
  1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

          [D]
          [N]
          [Z]
  [M] [C] [P]
  1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
'''

import sys

def main():
    stk = [[] for _ in range(int(sys.argv[2]))]
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for i in range(int(sys.argv[3])):
            line = f.readline()
            for i, c in enumerate(line[1::4]):
                if c.isalpha():
                    stk[i].append(c)
        
        stk = list(map(lambda x: list(reversed(x)), stk))

        # skip the number line
        f.readline()
        # skip the space line
        f.readline()

        for line in f:
            amount, from_i, to_i = map(int, line.split()[1::2])
            tmp = []
            for k in range(amount):
                tmp.append(stk[from_i-1].pop())
            stk[to_i-1] += tmp[::-1]
        
    out = []
    for s in stk:
        out.append(s[-1])
                
    with open(sys.argv[4], 'w', encoding='utf-8') as f:
        f.write(f'{"".join(out)}\n')

if __name__ == "__main__":
    main()