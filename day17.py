import sys
from collections import defaultdict

def print_grid():
    global underground
    global lowest_y
    f = 0
    t = 0
    if lowest_y <= 50:
        f = 0
        t = 100
    else:
        f = lowest_y - 50
        t = lowest_y + 50
    for row in range(f,t):
        c = ""
        for ch in underground[row]:
            c += ch
        print(c)

underground = []
max_y = 0

if sys.argv[2] == '1':
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
else:
    for line in open(sys.argv[1]):
        row = []
        for c in line.strip():
            row.append(c)
        underground.append(row)
    max_y = 13

flows = [(0,underground[0].index('+'))]

seen_flows = defaultdict(int)
seen_flows[(0,underground[0].index('+'))] = 1

queued_flows = set()
lowest_y = 0
while flows:
    # new_flows = set()
    # print(flows)
    for flow in flows:
        print_grid()
        input()
        x = flow[0]
        y = flow[1]
        if underground[x+1][y] == '.':
            queued_flows.add((x+1,y))
            underground[x+1][y] = '|'
        else:
            underground[x][y] = '~'
            curr_y = y - 1
            box_sit = 0
            while underground[x][curr_y] != '#' and underground[x + 1][curr_y] != '.' and (x,curr_y) not in seen_flows:
                underground[x][curr_y] = '~'
                curr_y -= 1
            if underground[x + 1][curr_y] == '.':
                box_sit += 1
                underground[x][curr_y] = '|'
                queued_flows.add((x,curr_y))

            curr_y = y + 1
            while underground[x][curr_y] != '#' and underground[x + 1][curr_y] != '.' and (x,curr_y) not in seen_flows:
                underground[x][curr_y] = '~'
                curr_y += 1
            if underground[x + 1][curr_y] == '.':
                box_sit += 1
                underground[x][curr_y] = '|'
                queued_flows.add((x,curr_y))
            if box_sit == 0:
                if underground[x-1][y] == '|':
                    queued_flows.add((x-1,y))
                else:
                    queued_flows.add((x-1,underground[x-1].index('|')))

    flows = []
    lowest_y = 99999
    for f in queued_flows:
        if f[0] < lowest_y:
            lowest_y = f[0]
    # print(lowest_y)

    new_queue = set()
    for f in queued_flows:
        seen_flows[f] += 1
        if f[0] != max_y and f[0] == lowest_y:
            flows.append(f)
        else:
            new_queue.add(f)

    queued_flows = new_queue


count = 0
for x in range(len(underground)):
    for y in range(len(underground[0])):
        if underground[x][y] == '|' or underground[x][y] == '~':
            count += 1

#print_grid()
print(count)
