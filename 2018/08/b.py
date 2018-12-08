
def go(data):
    if len(data) == 0:
        return 0
    nc = data.pop(0)
    nm = data.pop(0)
    s = 0
    if nc > 0:
        cn = []
        # list of all child values
        for _ in range(nc):
            cn.append(go(data))
        # read metadata as indices
        for _ in range(nm):
            i = data.pop(0) - 1
            if i < len(cn):
                s += cn[i]
    else:
        # no children - just add up metadata
        for _ in range(nm):
            s += data.pop(0)
    return s

with open('input', 'r') as f:
    for n in f:
        print(go(list(map(int, n.strip().split()))))
