import sys
from collections import defaultdict
from time import sleep

players = int(sys.argv[1])
last_marble = int(sys.argv[2])

marbles = [0]
scores = defaultdict(int)
curr_index = 1

for i in range(1, last_marble+1):
    if i % 23 == 0:
        to_remove = curr_index - 7
        scores[i%players] += i + marbles[to_remove]
        del marbles[to_remove]
        curr_index -= 7
        if curr_index < 0:
            curr_index += len(marbles) + 1
    elif curr_index == len(marbles):
        marbles.append(i)
    else:
        curr_index += 2
        if curr_index > len(marbles):
            curr_index = 1
        marbles.insert(curr_index,i)

print(max(scores.values()))
