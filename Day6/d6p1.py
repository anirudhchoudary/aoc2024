def read_file(file_name):
    with open(file_name, 'r') as f:
        grid = [list(line.strip()) for line in f]
    return grid

def move(grid, start_row, start_col):
    direction = "UP"
    current_row, current_col = start_row, start_col
    rows = len(grid)
    cols = len(grid[0])

    while 0 <= current_row < rows and 0 <= current_col < cols:
        if direction == "UP":
            while current_row > 0 and grid[current_row - 1][current_col] != "#":
                current_row -= 1
                grid[current_row][current_col] = "X"
            if current_row - 1 < 0:
                break
            direction = "RIGHT"

        elif direction == "RIGHT":
            while current_col + 1 < cols and grid[current_row][current_col + 1] != "#":
                current_col += 1
                grid[current_row][current_col] = "X"
            if current_col + 1 == cols:
                break
            direction = "DOWN"

        elif direction == "DOWN":
            while current_row + 1 < rows and grid[current_row + 1][current_col] != "#":
                current_row += 1
                grid[current_row][current_col] = "X"
            if current_row + 1 == rows:
                break
            direction = "LEFT"

        elif direction == "LEFT":
            while current_col > 0 and grid[current_row][current_col - 1] != "#":
                current_col -= 1
                grid[current_row][current_col] = "X"
            if current_col - 1 < 0:
                break
            direction = "UP"

        if not (0 <= current_row < rows and 0 <= current_col < cols):
            break

    return grid

def count_x(grid):
    total_x = sum(row.count("X") for row in grid)
    return total_x

def find_xcnt(file_name):
    grid = read_file(file_name)
    start_row, start_col = None, None
    for i, row in enumerate(grid):
        if "^" in row:
            start_row, start_col = i, row.index("^")
            break

    if start_row is None or start_col is None:
        return

    grid[start_row][start_col] = "X"
    grid = move(grid, start_row, start_col)
    result = count_x(grid)

    for row in grid:
        print("".join(row))

    print(f"Final 'X' count: {result}")

file_name = "d6p1-input.txt"
find_xcnt(file_name)
