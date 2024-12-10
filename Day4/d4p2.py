def read_grid(file_name):
    grid = []
    with open(file_name, 'r') as file:
        for line in file:
            grid.append(line.strip())
    return grid


def count_x_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def is_x_pattern(r, c):
        if grid[r][c] == word[1]:
            if (grid[r - 1][c - 1] == word[0] and grid[r + 1][c + 1] == word[2]) and (grid[r - 1][c + 1] == word[0] and grid[r + 1][c - 1] == word[2]):
                return True
            elif (grid[r - 1][c - 1] == word[2] and grid[r + 1][c + 1] == word[0]) and (grid[r - 1][c + 1] == word[2] and grid[r + 1][c - 1] == word[0]):
                return True
            elif (grid[r - 1][c - 1] == word[0] and grid[r + 1][c + 1] == word[2]) and (grid[r - 1][c + 1] == word[2] and grid[r + 1][c - 1] == word[0]):
                return True
            elif (grid[r - 1][c - 1] == word[2] and grid[r + 1][c + 1] == word[0]) and (grid[r - 1][c + 1] == word[0] and grid[r + 1][c - 1] == word[2]):
                return True

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if is_x_pattern(r, c):
                count += 1

    return count


file_name = "d4p1-input.txt"
word_to_search = "MAS"

grid = read_grid(file_name)

x_occurrences = count_x_occurrences(grid, word_to_search)

print(f"The word '{word_to_search}' forms an 'X' pattern {x_occurrences} time(s) in the grid.")
