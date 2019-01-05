import re
import sys
from collections import namedtuple
import ehoc as e

r1 = r'position=<(.*),(.*)> velocity=<(.*),(.*)>'
Star = namedtuple('Star', ['p', 'v'])


def extract(raw):
    mg = re.match(r1, raw)
    x = int(mg.group(1).strip())
    y = int(mg.group(2).strip())
    dx = int(mg.group(3).strip())
    dy = int(mg.group(4).strip())
    if 0:
        if mg.group(1) == '-':
            x = -1*x
        if mg.group(3) == '-':
            y = -1*y
        if mg.group(5) == '-':
            dx = -1*dx
        if mg.group(7) == '-':
            dy = -1*dy
    return x, y, dx, dy


def tick(stars_l, reverse=False):
    # Updates coordinates in stars list in place
    for i, item in enumerate(stars_l):
        if reverse:
            item.v.dx *= -1
            item.v.dy *= -1
        stars_l[i] = Star(item.p.apply_v(item.v), item.v)


def read_stars():
    ret = []
    with open('input', 'r') as f:
        for line in f:
            x, y, dx, dy = extract(line.strip())
            ret.append(Star(e.Point(x, y), e.Vector(dx, dy)))
    return ret


stars = read_stars()
counter = 0
minima = sys.maxsize
while True:
    x0, x1, y0, y1 = e.get_bounding_lines([k.p for k in stars])
    area = (x0 - x1)*(y0 - y1)
    if area <= minima:
        minima = area
        # Note: Part 2 is the "counter" value
        # print('{}: {}'.format(counter, area))
    else:
        break
    tick(stars)
    counter += 1

tick(stars, reverse=True)
e.draw([k.p for k in stars])

