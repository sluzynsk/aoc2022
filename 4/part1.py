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

        if (r2_max >= r1_max) and (r2_min <= r1_min):
            pairs+=1
        elif (r1_max >= r2_max) and (r1_min <= r2_min):
            pairs+=1
        else:
            continue
f.close()

print(pairs)