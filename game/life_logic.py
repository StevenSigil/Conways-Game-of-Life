import numpy as np


def random_position(arr):
    # Random position to place active cell relative to board dimensions
    rows = arr.shape[0]
    cols = arr.shape[1]
    random_row = np.random.randint(0, rows)
    random_col = np.random.randint(0, cols)
    return random_row, random_col


def setup_random(arr):
    """Defining the amount of random positions."""
    count = 0
    while count < round(arr.size * .3):  # Adjusting the .3 will give different results.
        r_pos = random_position(arr)
        arr[r_pos] = 1
        count += 1
    return


def cell_check(arr):
    """For each tick of the clock, retrieve the alive positions (before determining if they are to stay alive)."""
    alive_positions = []
    dead_positions = []

    for row in range(0, arr.shape[0]):
        for col in range(0, arr.shape[1]):
            value = arr[row, col]
            if value == 1:
                alive_positions.append((row, col))
            else:
                dead_positions.append((row, col))
    return alive_positions, dead_positions


def find_neighbors(position):
    """Coordinates of the 8 neighboring cells relative to the cell being checked. tl = top-left, tt = top-top, etc..."""
    col_pos = position[1]
    row_pos = position[0]
    tl = int(row_pos - 1), int(col_pos - 1)
    tt = int(row_pos - 1), int(col_pos)
    tr = int(row_pos - 1), int(col_pos + 1)
    lt = int(row_pos), int(col_pos - 1)
    rt = int(row_pos), int(col_pos + 1)
    bl = int(row_pos + 1), int(col_pos - 1)
    bb = int(row_pos + 1), int(col_pos)
    br = int(row_pos + 1), int(col_pos + 1)
    return [tl, tt, tr, lt, rt, bl, bb, br]


def check_neighbors(arr, cell):
    """For each cell on the board, returns the count of their alive neighbors"""
    alive_neighbor_count = 0
    neighbor_positions = find_neighbors(cell)
    # Checks neighboring positions to determine if the position is a position or the edge of the board.
    valid_positions = [i for i in neighbor_positions if arr.shape[0] - 1 >= i[0] >= 0 and arr.shape[1] - 1 >= i[1] >= 0]
    for neighbor in valid_positions:
        if arr[neighbor] == 1:
            alive_neighbor_count += 1
    return alive_neighbor_count


def alive_rules(arr, row, column):
    """Rule 1
    Cell stays alive if 2 or 3 neighbors are alive.
    """
    n_count = check_neighbors(arr, (row, column))
    if n_count != 2 and n_count != 3:
        change_to_dead = row, column
        return "D", change_to_dead
    else:
        keep_alive = row, column
        return "A", keep_alive


def dead_rules(arr, row, column):
    """Rule 2
    A dead cell with three live neighbors is made alive.
    """
    n_count = check_neighbors(arr, (row, column))
    if n_count == 3:
        change_to_alive = row, column
        return "A", change_to_alive
    else:
        stay_dead = row, column
        return "D", stay_dead


def cell_killer(arr, cell):
    arr[cell[0], cell[1]] = 0


def cell_defibrillator(arr, cell):
    arr[cell[0], cell[1]] = 1


def update_grid(arr):
    """Runs each tick of the clock. Takes the cells current position and value and changes the value depending on
    the outcome of the rules.
    """
    alive_cells, dead_cells = cell_check(arr)

    # Holding lists for current gen cells after checking them against rules.
    gen2_dead_cells = []
    gen2_alive_cells = []

    for cell in alive_cells:
        # Send alive cells through 'alive rules' -> append results to list -> Do NOT have npArray change yet
        char, position = alive_rules(arr, cell[0], cell[1])
        if char == "D":
            gen2_dead_cells.append(position)
        elif char == "A":
            gen2_alive_cells.append(position)

    for cell in dead_cells:
        # Send dead cells through 'dead rules' -> append results to list -> Do NOT change array yet
        char, position = dead_rules(arr, cell[0], cell[1])
        if char == "A":
            gen2_alive_cells.append(position)
        elif char == "D":
            gen2_dead_cells.append(position)

    # Now the cells are identified, change (or not) their value accordingly.
    for cell in gen2_dead_cells:
        cell_killer(arr, cell)
    for cell in gen2_alive_cells:
        cell_defibrillator(arr, cell)

    return arr
