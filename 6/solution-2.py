'''
Advent of Code 2022
--- Part Two ---

Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

  mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
  bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
  nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
  nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
  zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

How many characters need to be processed before the first start-of-message marker is detected?
'''

import sys
from collections import Counter

def main():
    out = 0
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        packet = f.readline()
        cnt = Counter()
        j = 0
        for i in range(len(packet)):
            cnt[packet[i]] += 1
            while j < i and cnt[packet[i]] > 1:
                cnt[packet[j]] -= 1
                if cnt[packet[j]] == 0:
                  del cnt[packet[j]]
                j += 1
            if len(cnt.keys()) >= 14:
                out = i + 1
                break

    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(f'{out}\n')

if __name__ == "__main__":
    main()