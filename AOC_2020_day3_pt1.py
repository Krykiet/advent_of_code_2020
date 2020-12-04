input_file = open('day3_input.txt', 'r')
grid_lines = input_file.readlines()
grid_clean = []
tree_counter = 0
x = 0
y = 0


def slide():
    global x
    x += 3
    global y
    y += 1
    return


for line in range(0, len(grid_lines)):
    grid_clean.append(grid_lines[line].rsplit()[0])
grid = grid_clean
width = len(grid[0])  # width of the slope
length = len(grid)  # length of the slope
for line in grid_clean:
    if x >= width:  # going to the next slope on the right
        shift = x - width
        x = shift
    if y >= length:
        end = True
    elif line[x] is '#':  # meeting the tree
        tree_counter += 1
        slide()
    else:  # no tree
        slide()

print(tree_counter)
