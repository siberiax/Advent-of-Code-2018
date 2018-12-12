import sys
from collections import defaultdict

input = open(sys.argv[1]).read().strip().split()
data = list(map(lambda x: int(x), input))

children = []
quantities = []
children_flag = 1
quantity_flag = 0
metadata_flag = 0

parents_to_children = defaultdict(list)
nodes_to_metadata = defaultdict(list)

i = 0
metadata = 0
index = 0
curr_child = 0
while index < len(data):
    if children_flag:
        if children:
            parents_to_children[children[-1][0]].append(i)
        children.append([i, data[index]])
        i += 1
        children_flag = 0
        quantity_flag = 1
        index += 1
        continue
    elif quantity_flag:
        quantity_flag = 0
        quantities.append(data[index])
        if (children[-1][1] == 0):
            curr_child = children.pop()
            metadata_flag = 1
        else:
            children_flag = 1
        index += 1
        continue
    else:
        metadata_flag = 0
        points = quantities.pop()
        for x in range(index, index + points):
            metadata += data[x]
            if curr_child:
                nodes_to_metadata[curr_child[0]].append(data[x])
        index += points
        if(children):
            parent = children.pop()
            parent[1] -= 1
            if parent[1] > 0:
                children.append(parent)
                children_flag = 1
            else:
                curr_child = parent
                metadata_flag = 1

print(metadata)
r = list(range(i))
r.reverse()

node_to_value = defaultdict(int)
for node in r:
    if node not in parents_to_children:
        value = 0
        for x in nodes_to_metadata[node]:
            value += x
        node_to_value[node] = value
    else:
        value = 0
        for x in nodes_to_metadata[node]:
            if x <= len(parents_to_children[node]):
                selection = parents_to_children[node][x-1]
                value += node_to_value[selection]
        node_to_value[node] = value

print(node_to_value[0])
