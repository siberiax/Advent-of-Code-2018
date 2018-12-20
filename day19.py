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
    if registers[2] > 1000000:
        big_num = registers[2]
        break
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
    if instruction == 'mulr':
        registers[c] = registers[a] * registers[b]
    if instruction == 'setr':
        registers[c] = registers[a]
    if instruction == 'seti':
        registers[c] = a
    if instruction == 'gtrr':
        registers[c] = int(registers[a] > registers[b])
    if instruction == 'eqrr':
        registers[c] = int(registers[a] == registers[b])
    registers[ip] += 1
    curr_inst = registers[ip]

if big_num:
    half = big_num//2
    sum = 0
    for i in range(1,big_num+1):
        if not big_num % i and i < big_num//i:
            sum += i
            sum += big_num//i
    registers[0] = sum

print(registers[0])













































#asdf
