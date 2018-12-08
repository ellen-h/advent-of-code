lower = []

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
        lower = set([c for c in line.strip() if c.islower()])
        polymer = list(line.strip())
        checkpoint = 0
        print(len(polymer))
        for _ in range(len(polymer)):
            if checkpoint >= len(polymer) - 1:
                break
            checkpoint = go(polymer, checkpoint)
        print(len(polymer))
