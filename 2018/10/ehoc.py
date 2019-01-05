
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def apply_v(self, v):
        return Point(self.x + v.dx, self.y + v.dy)


class Vector:

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


def get_bounding_lines(point_l):
    '''
    Accepts a list of Point objects
    Returns top x, bottom x, left y, right y
    '''
    min_x = min(point_l, key=lambda k: k.x).x
    max_x = max(point_l, key=lambda k: k.x).x
    min_y = min(point_l, key=lambda k: k.y).y
    max_y = max(point_l, key=lambda k: k.y).y
    return min_x, max_x, min_y, max_y


def draw(point_l):
    '''
    Accepts a list of Point objects
    Draws a grid only as big as needed to include all Point coordinates
    '''
    x0, x1, y0, y1 = get_bounding_lines(point_l)
    for y in range(y0, y1+1):
        for x in range(x0, x1+1):
            if Point(x, y) in point_l:
                print('#', end='')
                # print('{},{}'.format(x, y), end='')
            else:
                print('.', end='')
                # print('  .  ', end='')
        print()

