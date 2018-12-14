import sys
from collections import deque

recipes = [3,7]

elf1 = 0
elf2 = 1

iterations = sys.argv[1]

final = deque()
for c in iterations:
    final.append(int(c))

flen = len(final)

curr = deque()
curr.append(3)
curr.append(7)

length = 2
while curr != final:
    new = recipes[elf1] + recipes[elf2]
    if new < 10:
        recipes.append(new)
        curr.append(new)
        length += 1
        if len(curr) > flen:
            curr.popleft()
        if curr == final:
            break
    else:
        recipes.append(1)
        curr.append(1)
        length += 1
        if len(curr) > flen:
            curr.popleft()
        if curr == final:
            break
        length += 1
        recipes.append(new % 10)
        curr.append(new % 10)
        if len(curr) > flen:
            curr.popleft()
        if curr == final:
            break
    elf1 = (elf1 +1 + recipes[elf1]) % length
    elf2 = (elf2 + 1 + recipes[elf2]) % length

print(length - flen)
