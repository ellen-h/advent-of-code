lower = []
units = {}

def will_react(a, b):
    if a.lower() == b.lower():
        if (a in lower) != (b in lower):
            return True
    return False

def go(polymer, checkpoint):
    a = polymer[checkpoint]
    b = polymer[checkpoint+1]
    if will_react(a, b):
        del polymer[checkpoint+1]
        del polymer[checkpoint]
        return checkpoint - 1
    return checkpoint + 1

with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        lower = set([c for c in line if c.islower()])
        for u in lower:
            tmpline = line.replace(u, '').replace(u.upper(), '')
            polymer = list(tmpline)
            checkpoint = 0
            for _ in range(len(polymer)):
                if checkpoint >= len(polymer) - 1:
                    break
                checkpoint = go(polymer, checkpoint)
            units[u] = len(polymer)

ol = sorted(units.items(), key=lambda x: (x[1]))
print(ol[0][1])
