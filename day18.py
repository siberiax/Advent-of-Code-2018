import sys
from copy import deepcopy

def print_area(area):
    for y in area:
        row = ""
        for x in y:
            row += x
        print(row)

area = []

for line in open(sys.argv[1]):
    row = []
    for c in line.strip():
        row.append(c)
    area.append(row)

seen_areas = []

for minute in range(1000):
    new_area = deepcopy(area)
    for x in range(len(area)):
        for y in range(len(area[x])):
            to_check = []
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if i >= 0 and j >= 0 and i < len(area) and j < len(area[0]):
                        if i == x and j == y:
                            continue
                        else:
                            to_check.append((i,j))
            tree_count = 0
            lumberyard_count = 0
            for coord in to_check:
                if area[coord[0]][coord[1]] == '|':
                    tree_count += 1
                elif area[coord[0]][coord[1]] == '#':
                    lumberyard_count += 1

            if area[x][y] == '.':
                if tree_count >= 3:
                    new_area[x][y] = '|'
            elif area[x][y] == '|':
                if lumberyard_count >= 3:
                    new_area[x][y] = '#'
            else:
                if tree_count >= 1 and lumberyard_count >= 1:
                    new_area[x][y] = '#'
                else:
                    new_area[x][y] = '.'
    area = new_area
    if area in seen_areas:
        x = minute - seen_areas.index(area)
        z = 1000000000 - minute
        z //= x
        final = 1000000000 - z * x - minute
        part1_and_part2 = [seen_areas[9],seen_areas[seen_areas.index(area) + final - 1]]
        break
    seen_areas.append(area)


for area in part1_and_part2:
    trees = 0
    lumberyard = 0
    for x in range(len(area)):
        for y in range(len(area[0])):
            if area[x][y] == '|':
                trees += 1
            elif area[x][y] == '#':
                lumberyard += 1

    print(trees * lumberyard)
