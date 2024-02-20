import random
from colorama import Fore, Back, Style

red = '\033[31m'
green = '\033[32m'
yellow = '\033[93m'
reset = '\033[0m'

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
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (coordinate[0] + i) >= 0 and (coordinate[0] + i) <= 9 and (
                    coordinate[1] + j) >= 0 and (coordinate[1] + j) <= 9 and main_grid[
                coordinate[1] + j][coordinate[0] + i] == 0:
                main_grid[coordinate[1] + j][coordinate[0] + i] = 8


def change_grid(ship_array, ship_code):
    for i in ship_array:
        main_grid[i[1]][i[0]] = ship_code
    for x in ship_array:
        change_adjacent_squares(x)


def place_ships(orientation, length, ship_code):
    ship_array_test = []
    if orientation == "h":
        x = random.randint(0, 9 - length)
        y = random.randint(0, 9)
        for i in range(length):
            ship_array_test.append([x + i, y])
    elif orientation == "v":
        x = random.randint(0, 9)
        y = random.randint(0, 9 - length)
        for i in range(length):
            ship_array_test.append([x, y + i])
    if check_ship_overlap(ship_array_test):
        change_grid(ship_array_test, ship_code)
    else:
        place_ships(orientation, length, ship_code)


def print_grid(grid):
    print("  1  2  3  4  5  6  7  8  9  10")
    iteration = 65
    for i in grid:
        string_i = str(i)
        string_i = string_i.replace("[", chr(iteration) + " ")
        string_i = string_i.replace("]", '')
        string_i = string_i.replace("'", "")
        string_i = string_i.replace(",", " ")
        string_i = string_i.replace("X", green + "X" + reset)
        string_i = string_i.replace("O", red + "O" + reset)

        string_i = string_i.replace("1", red + "1" + reset)

        print(string_i)
        iteration += 1


orientation_options = ['h', 'v']
place_ships(random.choice(orientation_options), 5, 1)
place_ships(random.choice(orientation_options), 4, 2)
place_ships(random.choice(orientation_options), 3, 3)
place_ships(random.choice(orientation_options), 3, 4)
place_ships(random.choice(orientation_options), 2, 5)

game_playing = True

while game_playing:
    print_grid(viewer_grid)
    coordinates = input("\nType the coordinates: ")
    try:
        y_value = ord(coordinates[0].upper()) - 65
        x_value = int(coordinates[1:]) - 1
        if not main_grid[y_value][x_value] in [0,8]:
            print("You got a hit!")
            viewer_grid[y_value][x_value] = "X"
            # ADD CODE THAT DETECTS CRASHES
            # ship_locations.remove([x_value, y_value])
        else:
            print("You got a miss!")
            viewer_grid[y_value][x_value] = "O"
    except:
        print(yellow + "Please format the coordinates correctly!" + normal)

print_grid(main_grid)
