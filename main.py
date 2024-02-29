import random

# Initialize various ANSI escape codes to display color in the terminal
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

# Contains all the true locations of the ships. Computer will place ships on this grid, right now it's empty
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


# When the computer places a ship, this function checks if it overlaps with any other ships
def check_ship_overlap(ship_array):
    # Check if the square occupied by the ship is empty or not
    for i in ship_array:
        if not main_grid[i[1]][i[0]] == 0:
            return False
    return True


# After placing a ship down, mark the "water" around it so that no other ship is placed adjacent to it (battleship rules)
def change_adjacent_squares(coordinate, ship_code):
    # i is change in x coordinate, and j is change in y coordinate
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Checking if the water that is adjacent to the ship is out of bounds
            if (coordinate[0] + i) >= 0 and (coordinate[0] + i) <= 9 and (
                    coordinate[1] + j) >= 0 and (coordinate[1] + j) <= 9 and main_grid[
                coordinate[1] + j][coordinate[0] + i] == 0:
                main_grid[coordinate[1] + j][coordinate[0] + i] = ship_code + 5


# Changes the main grid and places the ship on it, then marks all the adjacent squares using the change_adjacent_squares function
def change_grid(ship_array, ship_code):
    for i in ship_array:
        main_grid[i[1]][i[0]] = ship_code
    for x in ship_array:
        change_adjacent_squares(x, ship_code)


# PLaces ships using their orientation and length onto the main grid using the previous functions
def place_ships(orientation, length, ship_code):
    # The array is used to hold the x and y coordinates that the ship fills up
    ship_array_test = []
    if orientation == "h": # Horizontal ship
        # Randomly select a starting point for the ship that's in range of the grid
        x = random.randint(0, 9 - length)
        y = random.randint(0, 9)
        # Add the squares that the ship occupies to the ship_array_test array
        for i in range(length):
            ship_array_test.append([x + i, y])
    elif orientation == "v": # Vertical ship
        # Randomly select a starting point for the ship that's in range of the grid
        x = random.randint(0, 9)
        y = random.randint(0, 9 - length)
        # Add the squares that the ship occupies to the ship_array_test array
        for i in range(length):
            ship_array_test.append([x, y + i])
    # Check if the ship overlaps with any other ships using the function we already created
    if check_ship_overlap(ship_array_test):
        # Update the grid with the ship
        change_grid(ship_array_test, ship_code)
    else:
        # Since the ship doesn't fit in the grid, rerun the code to try again
        place_ships(orientation, length, ship_code)


# Prints a 2d array, which in this case is a battleship grid
def print_grid(grid):
    # Change each cell in the grid into a string
    string_grid = [[str(cell) for cell in row] for row in grid]
    # Print the coordinates at the top
    print("  1  2  3  4  5  6  7  8  9  10")
    # These are the coordinates that are displayed on the side
    row_values = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    # Display each row of the grid
    for i in range(len(string_grid)):
        # Display the coordinate, and format the row with the color
        print(row_values[i], '  '.join(string_grid[i]).replace("O", red+"O"+reset).replace("X", green+"X"+reset))


# Creating the ships using the place_ships function, with random orientation and a unique ship code
orientation_options = ['h', 'v']
place_ships(random.choice(orientation_options), 5, 1)
place_ships(random.choice(orientation_options), 4, 2)
place_ships(random.choice(orientation_options), 3, 3)
place_ships(random.choice(orientation_options), 3, 4)
place_ships(random.choice(orientation_options), 2, 5)

# Using the ship code to notate which ships have not been sunk yet
ships_still_alive = [1, 2, 3, 4, 5]

# Check to see if any ships have crashed and return if it has
def check_for_crashes():
    living_ships = []
    # This for loop searches for all living ships on the grid that occupy at least one square
    for i in main_grid:
        for j in i:
            if j in [1, 2, 3, 4, 5]:
                living_ships.append(j)
    # Remove duplicates
    living_ships = set(living_ships)
    # Array that creates a list of all dead ships
    crashed_ships = [x for x in ships_still_alive if x not in living_ships]
    # Check if any ships are crashed and return the appropriate value if they have
    if crashed_ships == []:
        return [False, crashed_ships]
    else:
        # If a ship has crashed, remove it from the ships that are still alive
        ships_still_alive.remove(crashed_ships[0])
        return [True, crashed_ships]

# Marks all the water around a ship with "." on the viewer grid
def reveal_boundary(square_code):
    for i in range(10):
        for j in range(10):
            if main_grid[i][j] == square_code + 5:
                viewer_grid[i][j] = "."

# Track some basic game stats
won_game = False
total_tries = 0

rules = input("Welcome to battleship! \n\nYour goal is to sink all the ships in 50 tries or less! \nThere are 5 ships on the board with lengths 5, 4, 3, 3, and 2. \nMake your guesses by guuessing their coordinates using 'A1' or 'b10'. \nShips aren't allowed to be directly next to each other. \nGood luck! Press enter to continue.")

while total_tries < 50 and won_game == False:
    print_grid(viewer_grid)
    # Get the coordinates from the player
    coordinates = input("\nType the coordinates: ")
    # Attempt to covert the coordinates into integers
    try:
        total_tries += 1
        # Convert letter into an index for the list
        y_value = ord(coordinates[0].upper()) - 65
        # Convert integer into an index for the list
        x_value = int(coordinates[1:]) - 1
        # Check if the coordinates have hit a ship(0,6,7,8,9,10 are all water)
        if not main_grid[y_value][x_value] in [0, 6, 7, 8, 9, 10]:
            print("You got a hit!")
            # Mark the water with an X to indicate a hit
            viewer_grid[y_value][x_value] = "X"
            main_grid[y_value][x_value] = "X"
            # Check to see if a ship has crashed
            crash_results = check_for_crashes()
            if crash_results[0]:
                print("You crashed an entire boat!")
                reveal_boundary(crash_results[1][0])
            if ships_still_alive == []:
                won_game = True
                break
        else:
            # Mark a miss on the grid
            print("You got a miss!")
            viewer_grid[y_value][x_value] = "O"
    except Exception as e:
        print(yellow + "Please format the coordinates correctly!" + reset)

# Final win statement
print_grid(viewer_grid)
if won_game:
    print(f"Congratulations, you won! It took you {total_tries} tries!")
else:
    print("Better luck next time!")