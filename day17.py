import sys
from collections import defaultdict

def print_grid():
    global underground
    for row in range(13):
        c = ""
        for ch in underground[row]:
            c += ch
        print(c)

clay_coord = defaultdict(int)
min_x = 99999
max_x = 0
max_y = 0
for line in open(sys.argv[1]):
    fields = line.strip().split(', ')

    first = fields[0].split('=')
    second = fields[1].split('=')
    x = 0
    y = 0
    if first[0] == 'x':
        x = first[1]
        y = second[1]
    else:
        x = second[1]
        y = first[1]
    nums = 0
    if '..' in y:
        nums = y.split('..')
        for i in range(int(nums[0]), int(nums[1]) + 1):
            clay_coord[(int(x),i)]
    else:
        nums = x.split('..')
        for i in range(int(nums[0]), int(nums[1]) + 1):
            clay_coord[(i,int(y))] = 1
# #
underground = []

for line in open(sys.argv[1]):
    row = []
    for c in line.strip():
        row.append(c)
    underground.append(row)

for clay in clay_coord:
    if clay[0] < min_x:
        min_x = clay[0]
    elif clay[0] > max_x:
        max_x = clay[0]
    elif clay[1] > max_y:
        max_y = clay[1]

for i in range(max_y +1):
    row = []
    for j in range(min_x - 1, max_x + 2):
        if i == 0 and j == 500:
            row.append('+')
        elif (j,i) in clay_coord:
            row.append('#')
        else:
            row.append('.')
    underground.append(row)

flows = [(0,underground[0].index('+'))]

while flows:
    new_flows = []
    for flow in flows:
        x = flow[0]
        y = flow[1]
        if underground[x+1][y] == '.':
            new_flows.append((x+1,y))
            underground[x+1][y] = '|'
        else:
            cont_now = False
            currx = x
            curry_min = y - 1
            while underground[currx][curry_min] != '#' and underground[currx + 1][curry_min] != '.':
                curry_min -= 1
            if underground[currx + 1][curry_min] == '.':
                new_flows.append((currx,curry_min))
                cont_now = True
            curry_max = y + 1
            while underground[currx][curry_max] != '#' and underground[currx + 1][curry_max] != '.':
                curry_max += 1
            if underground[currx + 1][curry_max] == '.':
                new_flows.append((currx,curry_max))
                cont_now = True
            if cont_now:
                for i in range(curry_min,curry_max+1):
                    underground[currx][i] = '|'
                continue
            b = True
            while b:
                print_grid()
                input()
                for i in range(curry_min + 1,curry_max):
                    underground[currx][i] = '|'
                currx -= 1
                curr_y = y - 1
                while curr_y != curry_min:
                    if underground[currx][curr_y] == '#':
                        curry_min = curr_y
                        break
                    curr_y -= 1
                curr_y = y + 1
                while curr_y != curry_max:
                    if underground[currx][curr_y] == '#':
                        curry_max = curr_y
                        break
                    curr_y += 1
                if underground[currx][curry_min] == '.':
                    b = False
                    i = curry_max - 1
                    while underground[currx][i] != '#' and underground[currx + 1][i] != '.':
                        underground[currx][i] = '|'
                        i -= 1
                    new_flows.append((currx,curry_min-1))
                    underground[currx][i] = '|'
                if underground[currx][curry_max] == '.':
                    b = False
                    i = curry_min+1
                    while underground[currx][i] != '#' and underground[currx + 1][i] != '.':
                        underground[currx][i] = '|'
                        i += 1
                    underground[currx][i] = '|'
                    new_flows.append((currx,i))

    flows = []
    for f in new_flows:
        if f[0] != max_y:
            flows.append(f)

count = 0
for x in range(len(underground)):
    for y in range(len(underground[0])):
        if underground[x][y] == '|':
            count += 1

#print_grid()
print(count)

































# asdf
