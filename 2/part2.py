#!/usr/bin/env python3

score = 0

with open("input") as f:
    while True:
        line = f.readline()
        if not line:
            break
        their_move, outcome = line.strip().split(" ")
        print(f"Their move: {their_move}, outcome: {outcome}")
        if their_move == "A":
            if outcome == "Y": # need a draw
                score += 4  # 1 for rock, 3 to draw
            elif outcome == "X": # need to lose
                score += 3  # 3 for scissors, 0 for loss
            else: # need to win
                score += 8  # 2 for paper, 6 for win
        elif their_move == "B":
            if outcome == "Y": # draw
                score += 5  # 2 for paper, 3 for draw
            elif outcome == "X": # lose
                score += 1  # 1 for rock, none for loss
            else: # win
                score += 9  # three for scissors, 6 for win
        else:  # their move is C for scissors
            if outcome == "Y": # draw
                score += 6  # 3 for scissors, 3 for draw
            elif outcome == "X": # lose
                score += 2 # 2 for paper, 0 for loss
            else: # win
                score += 7  # 1 for rock, 6 for win

f.close()

print(f"The final score is {score}")
