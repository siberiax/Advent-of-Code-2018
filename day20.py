import sys
from collections import defaultdict, deque

data = open(sys.argv[1]).read().strip()

rooms = defaultdict(list)

queued_coord = []
curr_coord = (0,0)
for c in data:
    x = curr_coord[0]
    y = curr_coord[1]
    if c == '^' or c == '$':
        continue
    else:
        if c == 'N':
            rooms[curr_coord].append((x,y+1))
            curr_coord = (x,y+1)
        elif c == 'E':
            rooms[curr_coord].append((x+1,y))
            curr_coord = (x+1,y)
        elif c == 'S':
            rooms[curr_coord].append((x,y-1))
            curr_coord = (x,y-1)
        elif c == 'W':
            rooms[curr_coord].append((x-1,y))
            curr_coord = (x-1,y)
        elif c == '(':
            queued_coord.append(curr_coord)
        elif c == ')':
            curr_coord = queued_coord.pop()
        else:
            curr_coord = queued_coord[-1]

to_search = deque([(0,0)])
seen = [(0,0)]
total = 0
over_1000 = 0
while to_search:
    if total >= 1000:
        over_1000 += len(to_search)
    l = len(to_search)
    new = []
    for coord in to_search:
        for loc in rooms[coord]:
            if loc not in seen:
                new.append(loc)
                seen.append(loc)
    for _ in range(l):
        to_search.popleft()
    for n in new:
        to_search.append(n)
    total += 1

print(total-1)
print(over_1000)
