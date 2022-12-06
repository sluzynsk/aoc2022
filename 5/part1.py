#!/usr/bin/env python3

stacks = []
columns = 0
row = []

with open("input") as f:
    lines = f.readlines()
f.close()

i = 0
for line in lines:
    if line[0] == '[':
        i += 1
        continue
    elif line.strip() == '':
        break

print(lines[i])
columns = max(lines[i])

y = 0
for line in lines[range(0,i-1)]:
    row[i-1] = line.strip().split(' ')
    print(row[i-1])



