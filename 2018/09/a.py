from collections import defaultdict

# input: 432 players; last marble is worth 71019 points
np = 432
hi = 71019
nm = hi + 1
circle = [0, 1]
curr_pos = 1
players = defaultdict(int)
curr_player = 0

for curr_pt in range(2, nm):
    curr_player = (curr_player+1) % np
    if curr_pt % 23 == 0:
        players[curr_player+1] += curr_pt
        curr_pos = (curr_pos - 7) % len(circle)
        players[curr_player+1] += circle[curr_pos]
        circle = circle[:curr_pos] + circle[curr_pos + 1:]
    else:
        curr_pos = ((curr_pos + 1) % len(circle)) + 1
        circle = circle[:curr_pos] + [curr_pt] + circle[curr_pos:]

ol = [x for x in sorted(players.items(), key=lambda x: x[1], reverse=True)]
print(ol[0])
