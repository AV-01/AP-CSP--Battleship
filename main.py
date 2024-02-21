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


def change_adjacent_squares(coordinate,ship_code):
    # i is change in x coordinate, and j is change in y coordinate
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (coordinate[0] + i) >= 0 and (coordinate[0] + i) <= 9 and (
                    coordinate[1] + j) >= 0 and (coordinate[1] + j) <= 9 and main_grid[
                coordinate[1] + j][coordinate[0] + i] == 0:
                main_grid[coordinate[1] + j][coordinate[0] + i] = ship_code+5


def change_grid(ship_array, ship_code):
    for i in ship_array:
        main_grid[i[1]][i[0]] = ship_code
    for x in ship_array:
        change_adjacent_squares(x,ship_code)


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
        print(string_i)
        iteration += 1

orientation_options = ['h', 'v']
place_ships(random.choice(orientation_options), 5, 1)
place_ships(random.choice(orientation_options), 4, 2)
place_ships(random.choice(orientation_options), 3, 3)
place_ships(random.choice(orientation_options), 3, 4)
place_ships(random.choice(orientation_options), 2, 5)

ships_still_alive = [1,2,3,4,5]
def check_for_crashes():
    living_ships = []
    for i in main_grid:
        for j in i:
            if j in [1,2,3,4,5]:
                living_ships.append(j)
    living_ships = set(living_ships)
    crashed_ships = [x for x in ships_still_alive if x not in living_ships]
    if crashed_ships == []:
        return [False, crashed_ships]
    else:
        ships_still_alive.remove(crashed_ships[0])
        return [True, crashed_ships]

def mark_adjacent_squares(square_code):
    for i in range(10):
        for j in range(10):
            if main_grid[i][j] == square_code+5:
                viewer_grid[i][j] = "."

game_playing = True
total_tries = 0

while game_playing:
    print_grid(viewer_grid)
    coordinates = input("\nType the coordinates: ")
    try:
        total_tries += 1
        y_value = ord(coordinates[0].upper()) - 65
        x_value = int(coordinates[1:]) - 1
        if not main_grid[y_value][x_value] in [0,6,7,8,9,10]:
            print("You got a hit!")
            viewer_grid[y_value][x_value] = "X"
            main_grid[y_value][x_value] = "X"
            crash_results = check_for_crashes()
            if crash_results[0]:
                print("You crashed an entire boat!")
                mark_adjacent_squares(crash_results[1][0])
            if ships_still_alive == []:
                game_playing = False
                break
        else:
            print("You got a miss!")
            viewer_grid[y_value][x_value] = "O"
    except Exception as e:
        print(yellow + "Please format the coordinates correctly!" + reset)

print_grid(viewer_grid)
print(f"Congratulations, you won! It took you {total_tries} tries!")
