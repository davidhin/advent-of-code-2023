with open("../../data/day11.txt") as f:
    data = [list(i) for i in f.read().splitlines()]


# 1. Find all rows and columns that should be expanded
expand_rows = []
for i in range(len(data)):
    if set(data[i]) == set("."):
        expand_rows.append(i)

expand_cols = []
for j in range(len(data[0])):
    col = [data[i][j] for i in range(len(data))]
    if set(col) == set("."):
        expand_cols.append(j)

# 2. Find coordinates of all galaxies
coords = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "#":
            coords.append((i, j))


# 3. Iterate through and find x/y differences, which is shortest path, accounting for
# expanded rows and columns
total = 0
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        x = coords[i]
        y = coords[j]
        dist = abs(x[0] - y[0]) + abs(x[1] - y[1])
        intersect_r = [i for i in expand_rows if i in range(*sorted([x[0], y[0]]))]
        intersect_c = [i for i in expand_cols if i in range(*sorted([x[1], y[1]]))]
        # print(x, y, dist, intersect_r, intersect_c)
        total += dist + (len(intersect_c + intersect_r) * 999999)


total
