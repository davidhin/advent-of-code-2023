# The code for this does not actually work.
# This results in just solving the LCM of [22199, 13207, 16579, 18827, 17141, 14893]

import re
from collections import defaultdict
from functools import reduce


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"[{self.left} : {self.right}]"


def parse_input(filepath):
    with open(filepath, "r") as file:
        content = file.read()
    content = content.splitlines()
    instructions = content.pop(0)
    pattern = r"(\w+) = \((\w+), (\w+)\)"
    node_defs = [re.match(pattern, i).groups() for i in content[1:]]
    node_map = {}
    for node_def in node_defs:
        node_map[node_def[0]] = Node(node_def[1], node_def[2])
    return instructions, node_map


instructions, nodes = parse_input("../../data/day8.txt")
len_instructions = len(instructions)
curr_nodes = [i for i in nodes if i[2] == "A"]
node_equations = {i: [] for i in curr_nodes}
eq_result_sets = {curr_node: set() for curr_node in curr_nodes}
cycle_offsets = {}

for curr_node in curr_nodes:
    seen = {}
    curr = curr_node
    for step in range(0, 500000):
        if curr in seen and step % len_instructions == 0:
            cycle_start = seen[curr]
            period = step - seen[curr]
            zs_in_cycle = [
                i - cycle_start for i in eq_result_sets[curr_node] if i >= cycle_start
            ]
            equation = [zs_in_cycle, period]
            node_equations[curr_node] = equation
            cycle_offsets[curr_node] = cycle_start
            # print(f"Cycle start: {cycle_start}")
            # print(f"Period: {period}")
            # print(f"Zs In Cycle: {zs_in_cycle}")
            # print(f"Equation: {equation}")
            # print(f"{step} {curr} {seen}")
            # print("\n")
            # break
        if curr not in seen:
            seen[curr] = step
        inst = instructions[step % len_instructions]
        if inst == "L":
            curr = nodes[curr].left
        if inst == "R":
            curr = nodes[curr].right
        if curr[2] == "Z":
            eq_result_sets[curr_node].add(step + 1)


# equations = [[2], 3], [[4], 5], [[0], 2]
equations = list(node_equations.values())

[min(list(i)) for i in eq_result_sets.values()]

equations = [[[min(list(i))], min(list(i))] for i in eq_result_sets.values()]

for step in range(0, 5000):
    for node, eq in node_equations.items():
        for i in eq[0]:
            eq_result_sets[node].add(i + step * eq[1] + cycle_offsets[node])
    intersections = reduce(set.intersection, eq_result_sets.values())
    if len(intersections) > 0:
        print(list(intersections)[0])
        break


# The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

# What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

# After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

# For example:

# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
# Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

# Step 0: You are at 11A and 22A.
# Step 1: You choose all of the left paths, leading you to 11B and 22B.
# Step 2: You choose all of the right paths, leading you to 11Z and 22C.
# Step 3: You choose all of the left paths, leading you to 11B and 22Z.
# Step 4: You choose all of the right paths, leading you to 11Z and 22B.
# Step 5: You choose all of the left paths, leading you to 11B and 22C.
# Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
# So, in this example, you end up entirely on nodes that end in Z after 6 steps.

# Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?
