def recurse(input, idx, cur_conseq, stack, verbose=0):

    if len(stack) > 0 and cur_conseq > stack[0]:
        return 0

    if len(stack) == 0 and cur_conseq > 0:
        return 0

    if idx == len(input):
        if (list([cur_conseq]) == list(stack)) or (cur_conseq == 0 and len(stack) == 0):
            return 1
        else:
            return 0

    if (input[idx] == "." or input[idx] == "?") and (
        len(stack) == 0 or cur_conseq == stack[0]
    ):
        modified_input_a = list(input)
        modified_input_a[idx] = "."
        return recurse("".join(modified_input_a), idx + 1, 0, stack[1:])

    if input[idx] == ".":
        if cur_conseq > 0 and len(stack) > 0 and cur_conseq != stack[0]:
            return 0
        return recurse(input, idx + 1, cur_conseq, stack)
    elif input[idx] == "#":
        return recurse(input, idx + 1, cur_conseq + 1, stack)
    elif input[idx] == "?":
        branch_a = 0
        if not (cur_conseq > 0 and len(stack) > 0 and cur_conseq != stack[0]):
            modified_input_a = list(input)
            modified_input_a[idx] = "."
            branch_a = recurse("".join(modified_input_a), idx + 1, cur_conseq, stack)

        modified_input_b = list(input)
        modified_input_b[idx] = "#"
        branch_b = recurse("".join(modified_input_b), idx + 1, cur_conseq + 1, stack)
        return branch_a + branch_b


with open("../../data/day12.txt") as f:
    data = f.read().splitlines()
    args = []
    for i in data:
        input_str, input_stack = i.split()
        args.append((input_str, [int(i) for i in input_stack.split(",")]))

sum([recurse(i[0], 0, 0, i[1]) for i in args])
