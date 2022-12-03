#!/usr/bin/env python3

def splitString(string):
    first_half = string[0:len(string)//2]
    second_half = string[len(string)//2:]
    return [first_half, second_half]

tally = 0

with open("input") as f:
    while True:
        line = f.readline()
        if not line:
            break
        part_1, part_2 = splitString(line)
        for char in part_1:
            if char in part_2:
                item = char

        if item.islower():
            item_value = ord(item)-96
        else:
            item_value = ord(item.lower())-70
        print(f"{item},{item_value}")
        tally += item_value
f.close()

print(f"total: {tally} ")





