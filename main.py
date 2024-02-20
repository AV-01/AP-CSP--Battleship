import random

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
main_grid = [
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

def check_ship_overlap(ship_array):
    for i in ship_array:
        if not main_grid[i[1]][i[0]] == 0:
            return False
    return True

def change_adjacent_squares(coordinate):
    # i is change in x coordinate, and j is change in y coordinate
    for i in range(-1,2):
        for j in range(-1,2):
            if (coordinate[0]+i) >= 0 and (coordinate[0]+i) <= 9 and (coordinate[1]+j) >= 0 and (coordinate[1]+j) <= 9 and main_grid[coordinate[1]+j][coordinate[0]+i] == 0:
                main_grid[coordinate[1]+j][coordinate[0]+i] = 8
def change_grid(ship_array,ship_code):
    for i in ship_array:
        main_grid[i[1]][i[0]] = ship_code
    for x in ship_array:
        change_adjacent_squares(x)

def place_ships(orientation, length, ship_code):
    ship_array_test = []
    if orientation == "h":
        x = random.randint(0, 9-length)
        y = random.randint(0, 9)
        for i in range(length):
            ship_array_test.append([x + i, y])
    elif orientation == "v":
        x = random.randint(0, 9)
        y = random.randint(0, 9-length)
        for i in range(length):
            ship_array_test.append([x, y + i])
    if check_ship_overlap(ship_array_test):
        change_grid(ship_array_test,ship_code)
    else:
        place_ships(orientation, length, ship_code)

def print_grid(grid):
    print("  1  2  3  4  5  6  7  8  9  10")
    iteration = 65
    for i in grid:
        string_i = str(i)
        string_i = string_i.replace("[", chr(iteration) + " ")
        string_i = string_i.replace("]", '')
        string_i = string_i.replace("X",  "X")
        string_i = string_i.replace("O", "O")
        string_i = string_i.replace("'", "")
        string_i = string_i.replace(",", " ")
        print(string_i)
        iteration += 1

orientation_options = ['h','v']
place_ships(random.choice(orientation_options), 5, 1)
place_ships(random.choice(orientation_options), 4, 2)
place_ships(random.choice(orientation_options), 3, 3)
place_ships(random.choice(orientation_options), 3, 4)
place_ships(random.choice(orientation_options), 2, 5)

print_grid(main_grid)
