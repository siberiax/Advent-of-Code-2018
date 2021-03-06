import sys
from collections import defaultdict

curr_plants = defaultdict(chr)
state_changes = defaultdict(chr)

for line in open(sys.argv[1]):
    if '=>' in line:
        fields = line.strip().split(' => ')
        state_changes[fields[0]] = fields[1]
    else:
        for i in range(len(line.strip())):
            curr_plants[i] = line[i]

def stabilize_plants():
    lowest = 99999
    highest = 0
    for k in curr_plants.keys():
        if k < lowest and curr_plants[k] == '#':
            lowest = k
        if k > highest and curr_plants[k] == '#':
            highest = k
    for j in range(5):
        lowest -= 1
        curr_plants[lowest] = '.'
        highest += 1
        curr_plants[highest] = '.'
    return lowest,highest

prev_new = defaultdict(chr)
for i in range(1000):
    new_state = defaultdict(chr)
    start, end = stabilize_plants()
    for x in range(start+2,end-2):
        segment = curr_plants[x-2] + curr_plants[x-1] + curr_plants[x] + curr_plants[x+1] + curr_plants[x+2]
        new_state[x] = state_changes[segment]
    curr_plants = new_state
    if prev_new.values() == new_state.values():
        break
    prev_new = new_state

final = 0
for el in curr_plants.keys():
    if curr_plants[el] == '#':
        final += el + 50000000000 - i - 1
print(final)
