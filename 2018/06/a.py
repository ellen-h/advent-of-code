from collections import defaultdict

with open('input', 'r') as f:
    input_coords = []
    coord_areas = defaultdict(list)
    infinites = {}
    for line in f:
        input_coords.append((
            int(line.split(',')[0].strip()),
            int(line.split(',')[1].strip())
        ))
    max_x = int(max(input_coords, key=lambda item:int(item[0]))[0])
    max_y = int(max(input_coords, key=lambda item:int(item[1]))[1])
    min_x = int(min(input_coords, key=lambda item:int(item[0]))[0])
    min_y = int(min(input_coords, key=lambda item:int(item[1]))[1])

    # we check only the coords in the box
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (x,y) in input_coords: continue
            distance_to_coord = defaultdict(list)
            for p in input_coords:
                dist = abs(x-p[0]) + abs(y-p[1])
                distance_to_coord[dist].append(p)
            # get the shortest distance, toss it if a tie.
            for k,v in sorted(distance_to_coord.items()):
                if k > 0:
                    if len(v) == 1:
                        # assign this point as closest to this coord
                        coord_areas[v[0]].append((x,y))
                        # check if it hits the edge
                        if x in (min_x, max_x) or y in (min_y, max_y):
                            infinites[v[0]] = True
                    break

ans = [x for x in sorted(coord_areas.items(), key=lambda x: len(x[1]), reverse=True) if x[0] not in infinites][0]
print(len(ans[1])+1)
