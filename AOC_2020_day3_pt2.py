input_file = open('day3_input.txt', 'r')
grid_lines = input_file.readlines()
grid_clean = []
coordinates = [0, 0]


def slide(right, down):
    coordinates[0] += right
    coordinates[1] += down
    return coordinates


for line in range(0, len(grid_lines)):
    grid_clean.append(grid_lines[line].rsplit()[0])
grid = grid_clean
width = len(grid[0])  # width of the slope
length = len(grid)  # length of the slope


def toboggan(right, down):
    tree_counter = 0
    for level in grid_clean[::down]:
        if coordinates[0] >= width:  # going to the next slope on the right
            shift = coordinates[0] - width
            coordinates[0] = shift

        if level[coordinates[0]] is '#':  # meeting the tree
            tree_counter += 1
            slide(right, down)
        else:  # no tree
            slide(right, down)
    print(tree_counter)
    reset()
    return tree_counter


def reset():
    coordinates[0] = 0
    coordinates[1] = 0


print(toboggan(3, 1)*toboggan(1, 1)*toboggan(5, 1)*toboggan(7, 1)*toboggan(1, 2))
