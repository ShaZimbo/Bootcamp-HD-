import random

# Function to generate grid
def make_grid(width, hight):
    return[["-" for _ in range(width)] for _ in range(hight)]


def grid(width, hight, max_hash):
    grid = make_grid(width, hight)
    
    for h in range(hight):
        num_hash = random.randint(1, max_hash)
        hash_pos = random.sample(range(width), num_hash)

        for w in hash_pos:
            grid[h][w] = "#"
    return grid


# Function to identify relational positions
def get_surrounding_positions(grid, row, col):
    positions = {
        "nw": grid[row - 1][col - 1] 
        if row > 0 and col > 0 else None,
        "n": grid[row - 1][col] 
        if row > 0 else None,
        "ne": grid[row - 1][col + 1] 
        if row > 0 and col < len(grid[0]) - 1 else None,
        "w": grid[row][col - 1] 
        if col > 0 else None,
        "center": grid[row][col],
        "e": grid[row][col + 1] 
        if col < len(grid[0]) - 1 else None,
        "sw": grid[row + 1][col - 1] 
        if row < len(grid) - 1 and col > 0 else None,
        "s": grid[row + 1][col] 
        if row < len(grid) - 1 else None,
        "se": grid[row + 1][col + 1] 
        if row < len(grid) - 1 and col < len(grid[0]) - 1 else None
    }
    return positions


# Set dimensions of grid and number of hashes
random_grid = grid (15, 15, 5)

# Check rows in grid
for row_index, row in enumerate(random_grid):
    # Check cells in each row
    for col_index, cell in enumerate(row):
        # if there is no mine in cell
        if cell != "#":
            mines = 0
            surrounding_positions = get_surrounding_positions(
                random_grid, row_index, col_index)
            # Add 1 for each # in surrounding cells
            for _ in surrounding_positions.values():
                if _ == "#":
                    mines += 1
            random_grid[row_index][col_index] = str(mines)
for row in random_grid:
    print(" ".join(row))
