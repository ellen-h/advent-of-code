from collections import Counter
import itertools as it
data = open('input', 'r')
inputs = [r.strip() for r in data]
xinputs = [
'abcde',
'fghij',
'klmno',
'pqrst',
'fguij',
'axcye',
'wvxyz']

def run():
    for pair in it.combinations(inputs, 2):
        m = [len(set(i)) == 1 for i in zip(pair[0],pair[1])]
        c = Counter(m)
        if c[False] == 1:
            print(pair)
            s = pair[0]
            print(s[:m.index(False)] + s[m.index(False)+1:])

run()
