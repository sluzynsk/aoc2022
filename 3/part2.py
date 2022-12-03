#!/usr/bin/env python3

tally = 0

with open("input") as f:
    while True:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        if not line3:
            break

        group = [line1, line2, line3]
        
        longest = max(group, key = len)

        for char in longest:
            if char in line1 and char in line2 and char in line3:
                item = char
                break
        print(f"Badge for group is {item}")

        if item.islower():
            item_value = ord(item)-96
        else:
            item_value = ord(item.lower())-70
        print(f"{item},{item_value}")
        tally += item_value
f.close()

print(f"total: {tally} ")





