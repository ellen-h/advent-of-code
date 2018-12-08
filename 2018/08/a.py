def go(data):
    if len(data) == 0:
        return 0
    nc = data.pop(0)
    nm = data.pop(0)
    s = 0
    for i in range(nc):
        s += go(data)
    for j in range(nm):
        s += data.pop(0)
    return s

with open('input', 'r') as f:
    for n in f:
        print(go(list(map(int, n.strip().split()))))
