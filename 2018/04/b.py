from collections import defaultdict
import re

r1 = r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] ([a-zA-Z]+) (.*)'
r2 = r'#(\d+) .*'
rec = defaultdict(lambda: [0]*60)

def extract(raw):
    mg = re.match(r1, raw)
    mm = int(mg.group(5))
    ev = mg.group(6)
    rem = mg.group(7)
    return ev, mm, rem

with open('input', 'r') as f:
    ol = sorted(f)
    gid = ''
    start = 0
    for r in ol:
        ev, mm, rem = extract(r.strip())
        if ev == 'Guard':
            mg = re.match(r2, rem)
            gid = mg.group(1)
        elif ev == 'falls':
            start = mm
        elif ev == 'wakes':
            for i in range(start, mm):
                rec[gid][i]+=1
        else:
            print('unknown data')

    slacker = sorted([(max(v), k) for k,v in rec.items()], reverse=True)[0]
    slacker_id = slacker[1]
    slacker_sched = rec[slacker_id]
    slack_min = slacker_sched.index(max(slacker_sched))
    print(slack_min * int(slacker_id))
