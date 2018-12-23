import sys
import re
from collections import defaultdict

positions = {}
strongest = 0
strongest_coord = (0,0,0)
for line in open(sys.argv[1]):
    nums = [int(s) for s in re.findall(r'-?\d+', line)]
    positions[(nums[0],nums[1],nums[2])] = nums[3]
    if nums[3] > strongest:
        strongest = nums[3]
        strongest_coord = (nums[0],nums[1],nums[2])

in_range = 0
for pos in positions:
    r = abs(pos[0] - strongest_coord[0]) + abs(pos[1] - strongest_coord[1]) + abs(pos[2] - strongest_coord[2])
    if r <= strongest:
        in_range += 1

print(in_range)
