import datetime
import re
import sys

events = {}
times = []

for line in open(sys.argv[1]):
    date = re.search("\[(.*)\]", line)[1]
    dt = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
    times.append(dt)
    if "wakes" in line:
        events[dt] = 'w'
    elif "falls" in line:
        events[dt] = 'f'
    else:
        gnum = re.search("#([0-9]*)", line)[1]
        events[dt] = gnum

times.sort()

g_times = {}
curr_s = 0
curr_g = ""
for dt in times:
    ev = events[dt]
    if ev.isdigit():
        curr_g = ev
        if curr_g not in g_times:
            g_times[curr_g] = {}
    elif ev == 'f':
        curr_s = dt.minute
    else:
        for i in range(curr_s, dt.minute):
            curr_gt = g_times[curr_g]
            if i in curr_gt:
                curr_gt[i] += 1
            else:
                curr_gt[i] = 1
            g_times[curr_g] = curr_gt

top_g = 0
top_time = 0
top_t = 0
highest_minutes = 0
highest_t = 0
highest_g = 0

for g in g_times:
    curr = g_times[g]
    total = 0
    high = 0
    tt = 0
    for t in curr:
        total += curr[t]
        if curr[t] > high:
            high = curr[t]
            tt = t
    if total > top_time:
        top_g = int(g)
        top_time = total
        top_t = tt
    if high > highest_minutes:
        highest_g = int(g)
        highest_minutes = high
        highest_t = tt

print(top_g * top_t)
print(highest_g * highest_t)
