f = 0
seen = []
last_f = 0
while 1:
    d = f | 65536
    f = 733884
    b = d & 255
    f += b
    f &= 16777215
    f *= 65899
    f &= 16777215
    while d >= 256:
        d //= 256
        b = d & 255
        f += b
        f &= 16777215
        f *= 65899
        f &= 16777215

    if f in seen:
        break
    seen.append(f)
    last_f = f
print(seen[0])
print(last_f)

#debugging code
import sys

ip = 0
instructions = []
for line in open(sys.argv[1]):
    if "#ip" in line:
        ip = int(line.strip().split()[1])
    else:
        instructions.append(line.strip())

registers = [0, 0, 0, 0, 0, 0]

big_num = 0
curr_inst = 0
while curr_inst < len(instructions):
    fields = instructions[curr_inst].split()
    instruction = fields[0]
    a = int(fields[1])
    b = int(fields[2])
    c = int(fields[3])
    if instruction == 'addi':
        registers[c] = registers[a] + b
    if instruction == 'addr':
        registers[c] = registers[a] + registers[b]
    if instruction == 'muli':
        registers[c] = registers[a] * b
    if instruction == 'setr':
        registers[c] = registers[a]
    if instruction == 'seti':
        registers[c] = a
    if instruction == 'bani':
        registers[c] = registers[a] & b
    if instruction == 'bori':
        registers[c] = registers[a] | b
    if instruction == 'gtrr':
        registers[c] = int(registers[a] > registers[b])
    if instruction == 'gtir':
        registers[c] = int(a > registers[b])
    if instruction == 'eqrr':
        registers[c] = int(registers[a] == registers[b])
    if instruction == 'eqri':
        registers[c] = int(registers[a] == b)
    registers[ip] += 1
    print(instructions[curr_inst])
    print(registers)
    x = input()
    if len(x):
        registers[int(x.split()[0])] = int(x.split()[1])
    curr_inst = registers[ip]
