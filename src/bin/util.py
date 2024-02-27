def print_justified_rectangle(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    for row in data:
        print(" ".join(str(item).rjust(width) for item, width in zip(row, col_widths)))
