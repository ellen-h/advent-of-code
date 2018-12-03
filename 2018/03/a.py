from collections import defaultdict
data = open('input', 'r')
inputs = [r.strip() for r in data]
xinputs = [
'#1 @ 1,3: 4x4',
'#2 @ 3,1: 4x4',
'#3 @ 5,5: 2x2'
]

grid = defaultdict(int)

def run(inputs):
    for l in inputs:
        a = l.split()
        p = a[2].strip(':').split(',')
        z = a[3].split('x')
        mark(p, z)

def mark(p, z):
    x = int(p[0])
    y = int(p[1])
    w = int(z[0])
    h = int(z[1])
    for dx in range(w):
        for dy in range(h):
            grid[(x+dx, y+dy)] += 1

run(inputs)

count = 0
for k,v in grid.items():
    if v >= 2:
        count += 1

print(count)
