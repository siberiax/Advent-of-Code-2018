import sys
from collections import defaultdict

track = defaultdict(chr)
carts = []

i = 0
for line in open(sys.argv[1]):
    for j in range(len(line) - 1):
        c = line[j]
        if c != ' ':
            if c == '<':
                carts.append([i,j,0,0])
                track[(i,j)] = '-'
            if c == '^':
                carts.append([i,j,1,0])
                track[(i,j)] = '|'
            if c == '>':
                carts.append([i,j,2,0])
                track[(i,j)] = '-'
            if c == 'v':
                carts.append([i,j,3,0])
                track[(i,j)] = '|'
            track[(i,j)] = line[j]
    i += 1

def find_collisions():
    seen = []
    remove = []
    for cart in carts:
        curr_coord = (cart[1],cart[0])
        if curr_coord in seen:
            remove.append(curr_coord)
        seen.append(curr_coord)
    return remove

carts.sort()

while 1:
    if len(carts) == 1:
        print((carts[0][1],carts[0][0]))
        break
    to_remove = []
    for cart in carts:
        if (cart[1],cart[0]) not in to_remove:
            if cart[2] == 0:
                cart[1] -= 1
                curr_coord = (cart[0],cart[1])
                if track[curr_coord] == '\\':
                    cart[2] = 1
                elif track[curr_coord] == '/':
                    cart[2] = 3
                elif track[curr_coord] == '+':
                    if cart[3] == 0:
                        cart[2] = 3
                    elif cart[3] == 2:
                        cart[2] = 1
                    cart[3] += 1
                    cart[3] %= 3
            elif cart[2] == 1:
                cart[0] -= 1
                curr_coord = (cart[0],cart[1])
                if track[curr_coord] == '\\':
                    cart[2] = 0
                elif track[curr_coord] == '/':
                    cart[2] = 2
                elif track[curr_coord] == '+':
                    if cart[3] == 0:
                        cart[2] = 0
                    elif cart[3] == 2:
                        cart[2] = 2
                    cart[3] += 1
                    cart[3] %= 3
            elif cart[2] == 2:
                cart[1] += 1
                curr_coord = (cart[0],cart[1])
                if track[curr_coord] == '\\':
                    cart[2] = 3
                elif track[curr_coord] == '/':
                    cart[2] = 1
                elif track[curr_coord] == '+':
                    if cart[3] == 0:
                        cart[2] = 1
                    elif cart[3] == 2:
                        cart[2] = 3
                    cart[3] += 1
                    cart[3] %= 3
            else:
                cart[0] += 1
                curr_coord = (cart[0],cart[1])
                if track[curr_coord] == '\\':
                    cart[2] = 2
                elif track[curr_coord] == '/':
                    cart[2] = 0
                elif track[curr_coord] == '+':
                    if cart[3] == 0:
                        cart[2] = 2
                    elif cart[3] == 2:
                        cart[2] = 0
                    cart[3] += 1
                    cart[3] %= 3
            to_remove = find_collisions()
    new = []
    for cart in carts:
        if (cart[1],cart[0]) not in to_remove:
            new.append(cart)
    carts = new

    carts.sort()
