from collections import Counter
data = open('input', 'r')
inputs = [r.strip() for r in data]
xinputs = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab']

def run(inputs):
    threes = 0
    twos = 0
    for x in inputs:
        c = Counter(x)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1

    print(twos * threes)

run(inputs)
