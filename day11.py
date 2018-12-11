import sys
from collections import defaultdict
from time import sleep

grid_serial_number = int(sys.argv[1])

#grid = [[0 for i in range(300)] for j in range(300)]
grid = defaultdict(int)
fuel_levels = defaultdict(int)

for x in range(300):
    for y in range(300):
        fuel = (x + 11)
        fuel *= (y+1)
        fuel += grid_serial_number
        fuel *= (x + 11)
        if fuel < 100:
            fuel = 0
        else:
            fuel = int(str(fuel)[-3])
        fuel -= 5
        grid[(x,y)] = fuel
        fuel_levels[(x,y)] = fuel

highest = 0
high_coord = (0,0,0)


for r in range(1,301):
    to_pop = []
    for coord, fuel in fuel_levels.items():
        if fuel > highest:
            highest = fuel
            high_coord = (coord[0]+1,coord[1]+1,r)
        if coord[0] < 300 - r and coord[1] < 300 - r:
            x = coord[0]
            y = coord[1]
            for i in range(r):
                fuel += grid[(x+r,y+i)]
                fuel += grid[(x+i,y+r)]
            fuel += grid[(x+r,y+r)]
            fuel_levels[coord] = fuel
        else:
            to_pop.append(coord)
    for el in to_pop:
        fuel_levels.pop(el)

print(high_coord)
