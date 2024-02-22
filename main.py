import random
from colorama import Fore, Back, Style

red = '\033[31m'
green = '\033[32m'
yellow = '\033[93m'
reset = '\033[0m'

# This is what the player sees while playing the game. 0 means that it's just an empty cell with no guesses
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

# This is what the computer uses to place the ships, and it's used to mark where all
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

# While the computer places a ship, check if it overlaps with any other ships
def check_ship_overlap(ship_array):
    for i in ship_array:
        if not main_grid[i[1]][i[0]] == 0:
            return False
    return True

# After placing a ship down, mark the "water" around it so that no other ship is placed adjacent to it(battleship rules)
def change_adjacent_squares(coordinate,ship_code):
    # i is change in x coordinate, and j is change in y coordinate
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (coordinate[0] + i) >= 0 and (coordinate[0] + i) <= 9 and (
                    coordinate[1] + j) >= 0 and (coordinate[1] + j) <= 9 and main_grid[
                coordinate[1] + j][coordinate[0] + i] == 0:
                main_grid[coordinate[1] + j][coordinate[0] + i] = ship_code+5

# Changes the main grid and places the ship on it, then marks all the adjacent squares using the change_adjacent_squares function
def change_grid(ship_array, ship_code):
    for i in ship_array:
        main_grid[i[1]][i[0]] = ship_code
    for x in ship_array:
        change_adjacent_squares(x,ship_code)

# PLaces ships using their orientation and length onto the main grid using the previous functions.
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

# Prints a 2d array, which in this case is a battleship grid
def print_grid(grid):
    string_grid = [
        [str(cell) for cell in row]
        for row in viewer_grid
    ]
    print("  1  2  3  4  5  6  7  8  9  10")
    row_values = ["A","B","C","D","E","F","G","H","I","J"]
    for i in range(len(string_grid)):
        print(row_values[i],'  '.join(string_grid[i]))

# Creating the ships using the place_ships function
orientation_options = ['h', 'v']
place_ships(random.choice(orientation_options), 5, 1)
place_ships(random.choice(orientation_options), 4, 2)
place_ships(random.choice(orientation_options), 3, 3)
place_ships(random.choice(orientation_options), 3, 4)
place_ships(random.choice(orientation_options), 2, 5)

# Using the ship code to notate which ships have not been sunk yet
ships_still_alive = [1,2,3,4,5]

# Using the ship codes along with the ships_still_alive array to see which ships have crashed since the last time the function was called.
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
