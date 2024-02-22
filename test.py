viewer_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
red = '\033[31m'
green = '\033[32m'
yellow = '\033[93m'
reset = '\033[0m'
def print_grid(grid):
    string_grid = [
        [str(cell) for cell in row]
        for row in viewer_grid
    ]
    print("  1  2  3  4  5  6  7  8  9  10")
    row_values = ["A","B","C","D","E","F","G","H","I","J"]
    for i in range(len(string_grid)):
        print(row_values[i],'  '.join(string_grid[i]))

# for i in viewer_grid:
#     print(' '.join(i))
# viewer_grid = [
#     [str(cell) for cell in row]
#     for row in viewer_grid
# ]
# print(viewer_grid)
# print(' '.join(viewer_grid[0]))
print_grid(viewer_grid)