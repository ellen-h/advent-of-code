from collections import defaultdict, deque

# input: 432 players; last marble is worth 71019 points
np = 432
hi = 71019 * 100
nm = hi + 1
dq = deque([0])
players = defaultdict(int)
curr_player = 0

for curr_pt in range(1, nm):
    if curr_pt % 23 == 0:
        players[curr_player+1] += curr_pt
        dq.rotate(7)
        players[curr_player+1] += dq.pop()
        dq.rotate(-1)
    else:
        dq.rotate(-1)
        dq.append(curr_pt)

    curr_player = (curr_player+1) % np

ol = [x for x in sorted(players.items(), key=lambda x: x[1], reverse=True)]
print(ol[0])
