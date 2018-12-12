import sys
from collections import defaultdict

coords = defaultdict(tuple)
seen_vals = []
i = 1
for line in open(sys.argv[1]):
    coordinates = line.strip().split(', ')
    coords[i] = (int(coordinates[1]), int(coordinates[0]))
    seen_vals += [int(coordinates[1]), int(coordinates[0])]
    i += 1

length = max(seen_vals)
grid = [[0 for i in range(length + 1)] for j in range(length + 1)]

for coord in coords:
    loc = coords[coord]
    grid[loc[0]][loc[1]] = coord

vals = defaultdict(int)
edges = []
safe_spots = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        lowest_dist = 999999
        curr = 0
        dists = []
        for coord in coords:
            dist = abs(coords[coord][0] - x) + abs(coords[coord][1] - y)
            if dist:
                dists.append(dist)
                if dist < lowest_dist:
                    lowest_dist = dist
                    curr = coord
        total = sum(dists)
        if total < 10000:
            safe_spots += 1
        if x == 0 or x == length or y == 0 or y == length:
            edges.append(curr)
        if dists.count(min(dists)) == 1:
            grid[x][y] = curr
            vals[curr] += 1

high = 0
for coord, value in vals.items():
    if coord not in edges and value > high:
        high = value

print (high + 1)
print(safe_spots)
