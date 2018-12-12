import sys

polymer = open(sys.argv[1]).read().strip()
original_polymer = polymer

def reduce(polymer):
    i = 0
    length = len(polymer)
    while i < length-1:
        if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
            i -= 1
            length -= 2
            if i < 0:
                i = 0
                polymer = polymer[2:]
            else:
                polymer = polymer[:i+1] + polymer[i+3:]
        else:
            i += 1
    return(len(polymer))

print(reduce(polymer))

polymer = original_polymer

lowest = len(polymer)
for i in range(97,123):
    l = reduce(polymer.replace(chr(i),"").replace(chr(i-32),""))
    if l < lowest:
        lowest = l
print(lowest)
