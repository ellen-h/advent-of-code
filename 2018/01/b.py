data = open('input', 'r')
inputs = [int(r.strip()) for r in data]

def run():
    x = 0
    seen = {0:1}
    while 1:
        for op in inputs:
            x += op
            if x in seen:
                print(x)
                return
            seen[x] = 1

run()
