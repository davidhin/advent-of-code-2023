import re


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

steps = 0
curr = "AAA"
found = False
while not found:
    for inst in instructions:
        if inst == "L":
            curr = nodes[curr].left
        if inst == "R":
            curr = nodes[curr].right
        if curr == "ZZZ":
            found = True
            break
        steps += 1
print(steps)
