import sys
from collections import defaultdict
import re

operations = []

final_ops = []

before = []
after = []
ops = []
for line in open(sys.argv[1]):
    if "Before" in line:
        before = [int(s) for s in re.findall(r'\d+', line)]
    elif "After" in line:
        after = [int(s) for s in re.findall(r'\d+', line)]
        operations.append((ops,before,after))
        before = []
    elif line[0] != '\n':
        if before:
            ops = [int(s) for s in re.findall(r'\d+', line)]
        else:
            op = [int(s) for s in re.findall(r'\d+', line)]
            final_ops.append(op)

opcodes = defaultdict(list)

total_total = 0
for operation,before,after in operations:
    total = 0
    a = operation[1]
    b = operation[2]
    c = operation[3]

    possible = []

    if before[a] + before[b] == after[c]:
        possible.append('addr')
        total += 1

    if before[a] + b == after[c]:
        possible.append('addi')
        total += 1

    if before[a] * before[b] == after[c]:
        possible.append('mulr')
        total += 1

    if before[a] * b == after[c]:
        possible.append('muli')
        total += 1

    if before[a] & before[b] == after[c]:
        possible.append('banr')
        total += 1

    if before[a] & b == after[c]:
        possible.append('bani')
        total += 1

    if before[a] | before[b] == after[c]:
        possible.append('borr')
        total += 1

    if before[a] | b == after[c]:
        possible.append('bori')
        total += 1

    if before[a] == after[c]:
        possible.append('setr')
        total += 1

    if a == after[c]:
        possible.append('seti')
        total += 1

    if a > before[b] and after[c] == 1 or a <= before[b] and after[c] == 0:
        possible.append('gtir')
        total += 1

    if before[a] > b and after[c] == 1 or before[a] <= b and after[c] == 0:
        possible.append('gtri')
        total += 1

    if before[a] > before[b] and after[c] == 1 or before[a] <= before[b] and after[c] == 0:
        possible.append('gtrr')
        total += 1

    if before[a] == b and after[c] == 1 or before[a] != b and after[c] == 0:
        possible.append('eqri')
        total += 1

    if a == before[b] and after[c] == 1 or a != before[b] and after[c] == 0:
        possible.append('eqir')
        total += 1

    if before[a] == before[b] and after[c] == 1 or before[a] != before[b] and after[c] == 0:
        possible.append('eqrr')
        total += 1

    opcodes[operation[0]].append(possible)

    if total >= 3:
        total_total += 1

print(total_total)

ops = defaultdict(str)

#determine which opcode is which instruction
while len(ops) < 16:
    for opcode, values in opcodes.items():
        possible = values[0]
        for el in ops.values():
            if el in possible:
                possible.remove(el)
        if len(possible) == 1 and possible[0] not in ops:
            ops[opcode] = possible[0]

registers = [0,0,0,0]

for operation in final_ops:
    instruction = ops[operation[0]]
    a = operation[1]
    b = operation[2]
    c = operation[3]

    if instruction == 'addi':
        registers[c] = registers[a] + b
    if instruction == 'addr':
        registers[c] = registers[a] + registers[b]
    if instruction == 'muli':
        registers[c] = registers[a] * b
    if instruction == 'mulr':
        registers[c] = registers[a] * registers[b]
    if instruction == 'banr':
        registers[c] = registers[a] & registers[b]
    if instruction == 'bani':
        registers[c] = registers[a] & b
    if instruction == 'borr':
        registers[c] = registers[a] | registers[b]
    if instruction == 'bori':
        registers[c] = registers[a] | b
    if instruction == 'setr':
        registers[c] = registers[a]
    if instruction == 'seti':
        registers[c] = a
    if instruction == 'gtir':
        registers[c] = int(a > registers[b])
    if instruction == 'gtri':
        registers[c] = int(registers[a] > b)
    if instruction == 'gtrr':
        registers[c] = int(registers[a] > registers[b])
    if instruction == 'eqir':
        registers[c] = int(a == registers[b])
    if instruction == 'eqri':
        registers[c] = int(registers[a] == b)
    if instruction == 'eqrr':
        registers[c] = int(registers[a] == registers[b])

print(registers[0])
