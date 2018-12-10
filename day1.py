import sys

total = 0
seen = []
values = []
for line in open(sys.argv[1]):
    total += int(line.strip())
    seen.append(total)
    values.append(int(line.strip()))

print (total)
while 1:
    for value in values:
        total += value
        if total in seen:
            print(total)
            sys.exit()
        else:
            seen.append(total)
