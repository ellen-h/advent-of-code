from collections import defaultdict
data = open('input', 'r')
inputs = [r.strip() for r in data]
xinputs = [
'#1 @ 1,3: 4x4',
'#2 @ 3,1: 4x4',
'#3 @ 5,5: 2x2'
]

# map of how many claims each square has
countgrid = defaultdict(int)
# map of lists of claims each square has
claimgrid = defaultdict(list)
# map of cids and shares
idtracker = defaultdict(int)

def run(inputs):
    for l in inputs:
        a = l.split()
        p = a[2].strip(':').split(',')
        z = a[3].split('x')
        cid = a[0].strip('#')
        mark(cid, p, z)

def mark(currcid, p, z):
    x = int(p[0])
    y = int(p[1])
    w = int(z[0])
    h = int(z[1])
    idtracker[currcid] = 0
    for dx in range(w):
        for dy in range(h):
            if len(claimgrid[(x+dx, y+dy)]) > 0:
                for cid in claimgrid[(x+dx, y+dy)]:
                    # False is invalid, double claimed
                    idtracker[cid] += 1
                idtracker[currcid] += 1
            # track this square in any case
            countgrid[(x+dx, y+dy)] += 1
            claimgrid[(x+dx, y+dy)].append(currcid)

run(inputs)

for cid, v in idtracker.items():
    if v == 0:
        print(cid)
