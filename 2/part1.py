#!/usr/bin/env python3

score = 0

with open("input") as f:
    while True:
        line = f.readline()
        if not line:
            break
        their_move, my_move = line.strip().split(" ")
        print(f"Their move: {their_move}, my move: {my_move}")
        if their_move == "A":
            if my_move == "Y":
                score += 8  # 2 for paper, 6 to win
            elif my_move == "X":
                score += 4  # 1 for rock, 3 for draw
            else:
                score += 3  # three for scissors, none for loss
        elif their_move == "B":
            if my_move == "Y":
                score += 5  # 2 for paper, 3 for draw
            elif my_move == "X":
                score += 1  # 1 for rock, none for loss
            else:
                score += 9  # three for scissors, 6 for win
        else:  # their move is C for scissors
            if my_move == "Y":
                score += 2  # 2 for paper, none for loss
            elif my_move == "X":
                score += 7  # 1 for rock, 6 for win
            else:
                score += 6  # three for scissors, 3 for draw

f.close()

print(f"The final score is {score}")
