#!/usr/bin/env python3

data = []
pairs = 0

with open("input") as f:
    while True:
        line = f.readline()
        if not line:
            break
        range_1, range_2 = line.strip().split(',')

        r1_min_s, r1_max_s = range_1.split('-')
        r2_min_s, r2_max_s = range_2.split('-')

        r1_min = int(r1_min_s)
        r1_max = int(r1_max_s)
        r2_min = int(r2_min_s)
        r2_max = int(r2_max_s)

        r1 = range(r1_min, r1_max)
        r2 = range(r2_min, r2_max)

        output = range(max(r1.start, r2.start), min(r1.stop, r2.stop)+1)

        if len(output) > 0:
            pairs += 1
        
f.close()

print(pairs)

