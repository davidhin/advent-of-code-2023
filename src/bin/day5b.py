# Advent of Code Day 5b

# (79, 92)
# current_low: 79
# current_high: 92

# (50, 97) (offset: 52 - 50 = +2)
# new_low: 50
# new_high: 97

# if new_low <= current_low and new_high >= current_high
#   new_queue +
#      (current_low + offset, current_high + offset)
# if new_low <= current_low and new_high < current_high
#   new_queue +
#      (current_low + offset, new_high + offset)
#      (new_high + 1, current_high)
# if new_low > current_low and new_high >= current_high
#   new_queue +
#      (current_low, new_low - 1)
#      (new_low + offset, current_high + offset)
# if new_low > current_low and new_high < current_high
#   new_queue +
#      (current_low, new_low - 1)
#      (new_low + offset, new_high + offset)
#      (new_high + 1, current_high)


def map_range(current: tuple, new: tuple) -> list:
    """Map singular range to new ranges."""
    current_low, current_high = current
    new_low, new_high = [new[1], new[1] + new[2] - 1]
    offset = new[0] - new[1]
    old = []
    new = []

    if new_low > current_high or new_high < current_low:
        return [[(current_low, current_high)], []]

    if new_low <= current_low and new_high >= current_high:
        new.append((current_low + offset, current_high + offset))

    if new_low <= current_low and new_high < current_high:
        new.append((current_low + offset, new_high + offset))
        old.append((new_high + 1, current_high))

    if new_low > current_low and new_high >= current_high:
        new.append((new_low + offset, current_high + offset))
        old.append((current_low, new_low - 1))

    if new_low > current_low and new_high < current_high:
        old.append((current_low, new_low - 1))
        new.append((new_low + offset, new_high + offset))
        old.append((new_high + 1, current_high))

    return [old, new]


map_range((10, 20), (0, 10, 10))  # [0, 10]
map_range((10, 20), (0, 10, 5))  # [0, 5] [16, 20]
map_range((10, 20), (0, 15, 5))  # [0, 5] [10, 14]
map_range((10, 20), (0, 12, 2))  # [10, 11] [0, 2] [15, 20]
map_range((10, 20), (0, 21, 2))  # [10, 11] [0, 2] [15, 20]


def parse_input(filepath):
    """Parse advent of code input file."""
    with open(filepath, "r") as file:
        content = file.read()
    seeds = []
    maps = []
    current_map = []
    adding_to_map = False
    for line in content.splitlines() + [""]:
        if "seeds: " in line:
            seed_arr = line.split(":")[1].split()
            seed_arr = [int(i) for i in seed_arr]
            seeds += zip(seed_arr[::2], seed_arr[1::2])
        if "map:" in line:
            current_map = []
            adding_to_map = True
            continue
        if adding_to_map:
            if line == "":
                adding_to_map = False
                maps.append(current_map)
            else:
                current_map.append([int(i) for i in line.split()])

    return [(i[0], i[0] + i[1] - 1) for i in seeds], maps


seeds, maps = parse_input("../../data/day5a.txt")


def apply_map_group_to_seeds(seeds, map_group):
    seed_groups = list(seeds)
    new_groups = []
    for map_row in map_group:
        old_groups = []
        while len(seed_groups) > 0:
            seed_group = seed_groups.pop(0)
            old, new = map_range(seed_group, map_row)
            old_groups += old
            new_groups += new
        seed_groups = old_groups
    return seed_groups + new_groups


results = []
for seed_groups in seeds:
    mapped_seed_groups = [seed_groups]
    for map_group in maps:
        mapped_seed_groups = apply_map_group_to_seeds(mapped_seed_groups, map_group)
    results += mapped_seed_groups

print(f"Result: {min([i[0] for i in results])}")
