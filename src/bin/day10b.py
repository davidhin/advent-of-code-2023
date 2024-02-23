def parse_input(filepath):
    with open(filepath, "r") as file:
        content = file.read()
    content = content.splitlines()
    return [list(i) for i in content]


def find_start(graph):
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == "S":
                return row, col, 0


def print_justified_rectangle(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    for row in data:
        print(" ".join(str(item).rjust(width) for item, width in zip(row, col_widths)))


graph = parse_input("../../data/day10.txt")
dists = [["*" for _ in range(len(row))] for row in graph]
areas = [["*" for _ in range(len(row))] for row in graph]
start = find_start(graph)
bfs = [start]
height = len(graph)
width = len(graph[0])


def set_area(row, col, letter):
    if (row < 0) or (row == height) or (col < 0) or (col == width):
        return
    if areas[row][col] in ["S", "|", "-", "L", "J", "7", "F", "■"]:
        return
    areas[row][col] = letter


while len(bfs) > 0:
    cur_row, cur_col, dist = bfs.pop(0)
    dists[cur_row][cur_col] = dist
    curr_tile = graph[cur_row][cur_col]
    areas[cur_row][cur_col] = "■"  # curr_tile
    if curr_tile == "S":
        # Top
        if cur_row > 0 and graph[cur_row - 1][cur_col] in ["|", "7", "F"]:
            bfs.append((cur_row - 1, cur_col, dist + 1))
        # Bottom
        elif cur_row < (height - 1) and graph[cur_row + 1][cur_col] in ["|", "L", "J"]:
            bfs.append((cur_row + 1, cur_col, dist + 1))
        # Left
        elif cur_col > 0 and graph[cur_row][cur_col - 1] in ["-", "L", "F"]:
            bfs.append((cur_row, cur_col - 1, dist + 1))
        # Right
        elif cur_col < (width - 1) and graph[cur_row][cur_col + 1] in ["-", "J", "7"]:
            bfs.append((cur_row, cur_col + 1, dist + 1))
    if curr_tile == "|":
        # Top
        if cur_row > 0 and dists[cur_row - 1][cur_col] == "*":
            set_area(cur_row, cur_col + 1, "O")
            set_area(cur_row, cur_col - 1, "I")
            bfs.append((cur_row - 1, cur_col, dist + 1))
        # Bottom
        if cur_row < (height - 1) and dists[cur_row + 1][cur_col] == "*":
            set_area(cur_row, cur_col + 1, "I")
            set_area(cur_row, cur_col - 1, "O")
            bfs.append((cur_row + 1, cur_col, dist + 1))

    if curr_tile == "-":
        # Left
        if cur_col > 0 and dists[cur_row][cur_col - 1] == "*":
            set_area(cur_row + 1, cur_col, "I")
            set_area(cur_row - 1, cur_col, "O")
            bfs.append((cur_row, cur_col - 1, dist + 1))
        # Right
        if cur_col < (width - 1) and dists[cur_row][cur_col + 1] == "*":
            set_area(cur_row - 1, cur_col, "I")
            set_area(cur_row + 1, cur_col, "O")
            bfs.append((cur_row, cur_col + 1, dist + 1))

    if curr_tile == "L":
        # Top
        if cur_row > 0 and dists[cur_row - 1][cur_col] == "*":
            set_area(cur_row, cur_col - 1, "I")
            set_area(cur_row + 1, cur_col - 1, "I")
            set_area(cur_row + 1, cur_col, "I")
            set_area(cur_row - 1, cur_col + 1, "O")
            bfs.append((cur_row - 1, cur_col, dist + 1))
        # Right
        if cur_col < (width - 1) and dists[cur_row][cur_col + 1] == "*":
            set_area(cur_row, cur_col - 1, "O")
            set_area(cur_row + 1, cur_col - 1, "O")
            set_area(cur_row + 1, cur_col, "O")
            set_area(cur_row - 1, cur_col + 1, "I")
            bfs.append((cur_row, cur_col + 1, dist + 1))

    if curr_tile == "J":
        # Top
        if cur_row > 0 and dists[cur_row - 1][cur_col] == "*":
            set_area(cur_row + 1, cur_col, "O")
            set_area(cur_row + 1, cur_col + 1, "O")
            set_area(cur_row, cur_col + 1, "O")
            set_area(cur_row - 1, cur_col - 1, "I")
            bfs.append((cur_row - 1, cur_col, dist + 1))
        # Left
        if cur_col > 0 and dists[cur_row][cur_col - 1] == "*":
            set_area(cur_row + 1, cur_col, "I")
            set_area(cur_row + 1, cur_col + 1, "I")
            set_area(cur_row, cur_col + 1, "I")
            set_area(cur_row - 1, cur_col - 1, "O")
            bfs.append((cur_row, cur_col - 1, dist + 1))

    if curr_tile == "7":
        # Left
        if cur_col > 0 and dists[cur_row][cur_col - 1] == "*":
            set_area(cur_row - 1, cur_col, "O")
            set_area(cur_row - 1, cur_col + 1, "O")
            set_area(cur_row, cur_col + 1, "O")
            set_area(cur_row + 1, cur_col - 1, "I")
            bfs.append((cur_row, cur_col - 1, dist + 1))
        # Bottom
        if cur_row < (height - 1) and dists[cur_row + 1][cur_col] == "*":
            set_area(cur_row - 1, cur_col, "I")
            set_area(cur_row - 1, cur_col + 1, "I")
            set_area(cur_row, cur_col + 1, "I")
            set_area(cur_row + 1, cur_col - 1, "O")
            bfs.append((cur_row + 1, cur_col, dist + 1))

    if curr_tile == "F":
        # Bottom
        if cur_row < (height - 1) and dists[cur_row + 1][cur_col] == "*":
            set_area(cur_row - 1, cur_col, "O")
            set_area(cur_row - 1, cur_col - 1, "O")
            set_area(cur_row, cur_col - 1, "O")
            set_area(cur_row + 1, cur_col + 1, "I")
            bfs.append((cur_row + 1, cur_col, dist + 1))
        # Right
        if cur_col < (width - 1) and dists[cur_row][cur_col + 1] == "*":
            set_area(cur_row - 1, cur_col, "I")
            set_area(cur_row - 1, cur_col - 1, "I")
            set_area(cur_row, cur_col - 1, "I")
            set_area(cur_row + 1, cur_col + 1, "O")
            bfs.append((cur_row, cur_col + 1, dist + 1))

max([i for i in [i for j in dists for i in j] if i != "*"])

bfs_areas = []
for row in range(height):
    for col in range(width):
        if areas[row][col] != "O":
            continue
        bfs_areas.append((row, col))

while len(bfs_areas) > 0:
    row, col = bfs_areas.pop(0)
    areas[row][col] = "O"
    if (row < 0) or (row == height) or (col < 0) or (col == width):
        continue
    if areas[row][col] in ["S", "|", "-", "L", "J", "7", "F", "■"]:
        continue
    if areas[row + 1][col] == "*":
        bfs_areas.append((row + 1, col))

print_justified_rectangle(areas)

final_inner_count = 0
for row in range(height):
    for col in range(width):
        if areas[row][col] == "O":
            final_inner_count += 1

print(final_inner_count)

# You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the area enclosed by the loop?

# To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

# ...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ...........
# The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those regions marked:

# ...........
# .S-------7.
# .|F-----7|.
# .||OOOOO||.
# .||OOOOO||.
# .|L-7OF-J|.
# .|II|O|II|.
# .L--JOL--J.
# .....O.....
# In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

# ..........
# .S------7.
# .|F----7|.
# .||OOOO||.
# .||OOOO||.
# .|L-7F-J|.
# .|II||II|.
# .L--JL--J.
# ..........
# In both of the above examples, 4 tiles are enclosed by the loop.

# Here's a larger example:

# .F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...
# The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

# OF----7F7F7F7F-7OOOO
# O|F--7||||||||FJOOOO
# O||OFJ||||||||L7OOOO
# FJL7L7LJLJ||LJIL-7OO
# L--JOL7IIILJS7F-7L7O
# OOOOF-JIIF7FJ|L7L7L7
# OOOOL7IF7||L7|IL7L7|
# OOOOO|FJLJ|FJ|F7|OLJ
# OOOOFJL-7O||O||||OOO
# OOOOL---JOLJOLJLJOOO
# In this larger example, 8 tiles are enclosed by the loop.

# Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# Here are just the tiles that are enclosed by the loop marked with I:

# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJIF7FJ-
# L---JF-JLJIIIIFJLJJ7
# |F|F-JF---7IIIL7L|7|
# |FFJF7L7F-JF7IIL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# In this last example, 10 tiles are enclosed by the loop.

# Figure out whether you have time to search for the nest by calculating the area within the loop. How many tiles are enclosed by the loop?
