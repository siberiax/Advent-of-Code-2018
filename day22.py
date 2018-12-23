import sys
import heapq

def print_grid(grid):
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                row += '.'
            elif grid[y][x] == 1:
                row += '='
            else:
                row += '|'
        print(row)

depth = int(sys.argv[1])
target = tuple(sys.argv[2].split(','))
target = (int(target[0]),int(target[1]))

grid = [[0 for i in range(depth)] for j in range(depth)]
cave = [[0 for i in range(depth)] for j in range(depth)]

for y in range(depth):
    for x in range(depth):
        geo_index = 0
        if (x == 0 and y == 0) or (x == target[0] and y == target[1]):
            geo_index = 0
        elif x == 0:
            geo_index = y * 48271
        elif y == 0:
            geo_index = x * 16807
        else:
            geo_index = grid[y-1][x] * grid[y][x-1]
        geo_index += depth
        erosion = geo_index % 20183
        grid[y][x] = erosion
        cave[y][x] = erosion % 3

total_risk = 0
for y in range(target[1] + 1):
    for x in range(target[0] + 1):
        total_risk += cave[y][x]

print(total_risk)

queue = [(0,0,0,1)]
best_times = {}
target = (target[0], target[1], 1)
while queue:
    minutes, x, y, item = heapq.heappop(queue)
    if (x,y,item) in best_times and best_times[(x,y,item)] <= minutes:
        continue
    best_times[(x,y,item)] = minutes
    if (x,y,item) == target:
        print(minutes)
        break
    for i in range(3):
        if i != item and i != cave[y][x]:
            heapq.heappush(queue, (minutes + 7, x, y, i))

    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x = i + x
        new_y = j + y
        if new_x >= 0 and new_y >= 0 and cave[new_y][new_x] != item:
            heapq.heappush(queue, (minutes + 1, new_x, new_y, item))
