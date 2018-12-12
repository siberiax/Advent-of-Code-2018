import sys
from collections import defaultdict

steps = defaultdict(list)
steps2 = defaultdict(list)
before = []
after = []
for line in open(sys.argv[1]):
    fields = line.split()
    steps[fields[7]].append(fields[1])
    steps2[fields[7]].append(fields[1])
    before.append(fields[1])
    after.append(fields[7])

ready_chars = []
for c in before:
    if c not in after and c not in ready_chars:
        ready_chars.append(c)

ready_chars.sort()
ready_chars_copy = ready_chars
order_string = ""
while ready_chars:
    curr = ready_chars[0]
    order_string += curr
    ready_chars = ready_chars[1:]
    to_pop = []
    for key, value in steps.items():
        if curr in value:
            steps[key].remove(curr)
            if steps[key] == []:
                ready_chars += key
                to_pop.append(key)
    map(lambda key: steps.pop(key),to_pop)
    ready_chars.sort()

print(order_string)

workers = defaultdict(int)
seconds = 0

for c in ready_chars_copy:
    workers[c] = ord(c) - 4

queue = []
while len(workers):
    seconds += 1
    finished = []
    for worker in workers:
        if workers[worker] > 1:
            workers[worker] -= 1
        else:
            finished.append(worker)
    for el in finished:
        workers.pop(el)
    for finish in finished:
        to_pop = []
        for key, value in steps2.items():
            if finish in value:
                steps2[key].remove(finish)
                if steps2[key] == []:
                    queue.append(key)
                    to_pop.append(key)
        map(lambda key: steps2.pop(key),to_pop)
    for ready in queue:
        if len(workers) < 5:
            workers[queue[0]] = ord(queue[0]) - 4
            queue = queue[1:]

print(seconds)
