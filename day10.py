import sys
from collections import defaultdict
import re

coordinates_to_momentum = defaultdict(list)

i = 0
for line in open(sys.argv[1]):
    digits = [int(s) for s in re.findall(r'-?\d+', line)]
    coordinates_to_momentum[i] = [digits[0],digits[1],digits[2],digits[3]]
    i += 1

z = 0
while 1:
    new = defaultdict(tuple)
    y_min = 100000
    y_max = 0
    x_min = 100000
    x_max = 0
    coords = []
    i = 0
    good = 1
    for value in coordinates_to_momentum.values():
        x = value[0]
        y = value[1]
        if y > y_max:
            y_max = y
        if y < y_min:
            y_min = y
        if x > x_max:
            x_max = x
        if x < x_min:
            x_min = x
        coords.append((x, y))
        new[i] = [value[0] + value[2], value[1] + value[3], value[2], value[3]]
        i += 1
    if y_max - y_min <= 10:
        grid = []
        for j in range(y_min,y_max+1):
            row = ""
            for i in list(range(x_min,x_max+1)):
                if (i, j) in coords:
                    row += '#'
                else:
                    row += ' '
            grid.append(row)
        for el in grid:
            print(el)
        print(z)
        break
    coordinates_to_momentum = new
    z += 1
