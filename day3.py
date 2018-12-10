import sys

fabric = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    fabric.append(row)

claims = {}
for line in open(sys.argv[1]):
    fields = line.strip().split()
    area = fields[2][:-1].split(',')
    dims = fields[3].split('x')
    claim = int(fields[0][1:])
    claims[claim] = int(dims[0]) * int(dims[1])
    for i in range(int(dims[0])):
        for j in range(int(dims[1])):
            if fabric[int(area[0])+i][int(area[1])+j]:
                fabric[int(area[0])+i][int(area[1])+j] = '.'
            else:
                fabric[int(area[0])+i][int(area[1])+j] = claim

total = 0
ends = {}
for i in range(1000):
    for j in range(1000):
        piece = fabric[i][j]
        if piece == '.':
            total += 1
        else:
            if piece in ends:
                ends[piece] += 1
            else:
                ends[piece] = 1

print(total)

for claim in ends:
    if claim and claims[claim] == ends[claim]:
        print(claim)
