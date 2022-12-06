from collections import deque 

crates = []
with open('stacks.txt') as f:
    for i, line in enumerate(f):
        if line.strip() == "":
            end = i
        crates.append(line.rstrip("\n"))

numStacks = (len(crates[0]) + 1) // 4
stacks = {}

def moveToStacks(row):
    global stacks, numStacks
    j = 0
    k = 3
    for i in range(1,numStacks+1):
        if i not in stacks:
            stacks[i] = deque([])
        item = row[j:j+3]
        item = item.strip()
        if item != "":
            stacks[i].append(item)
        j = k + 1
        k = k + 4

for i in range(end - 1):
    moveToStacks(crates[i])

instructions = crates[end+1:]

def formatInstruction(ins):
    ins = ins.lstrip("move ")
    times = int(ins[0:2].rstrip())
    ins = ins[2:].lstrip(" from")
    first = int(ins[0])
    last = int(ins[-1])
    return [times, first, last]

final = []
for instruction in instructions:
    formatted = formatInstruction(instruction)

    for i in range(formatted[0]):
        popped = stacks[formatted[1]].popleft()
        stacks[formatted[2]].appendleft(popped)

for stack in stacks.items():
    final.append(stack[1][0])
# print(stacks)
print(final)