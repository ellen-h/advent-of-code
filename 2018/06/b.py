from collections import defaultdict

with open('input', 'r') as f:
    input_coords = []
    coord_areas = defaultdict(list)
    safe_zone = 0
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
            distance_to_coord = defaultdict(list)
            local_sum = 0
            for p in input_coords:
                dist = abs(x-p[0]) + abs(y-p[1])
                local_sum += dist
            if local_sum < 10000:
                safe_zone += 1

    print(safe_zone)
