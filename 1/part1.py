#!/usr/bin/env python3
import heapq


val = 0
elves = []

with open("input") as f:
    while True:
        line = f.readline()
        if not line:
            elves.append(val)
            val = 0
            break
        if line == '\n':
            elves.append(val)
            val = 0
        else:
            val += int(line)
f.close()
       
print(f"Part 1 answer: Elf with the most calories has {max(elves)}")

largest3 = heapq.nlargest(3, zip(elves))

val = 0
for item in largest3:
    val += item[0]

print(f"Part 2 answer: the top 3 combined have {val} calories")

