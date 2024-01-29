astr = input()
cur_pos = 1
for move in astr:
    if move == "A":
        if cur_pos == 1:
            cur_pos = 2
        elif cur_pos == 2:
            cur_pos = 1
    elif move == "B":
        if cur_pos == 2:
            cur_pos = 3
        elif cur_pos == 3:
            cur_pos = 2
    elif move == "C":
        if cur_pos == 1:
            cur_pos = 3
        elif cur_pos == 3:
            cur_pos = 1
print(cur_pos)