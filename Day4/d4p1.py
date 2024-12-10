def read_grid(file_name):
    grid = []
    with open(file_name, 'r') as file:
        for line in file:
            grid.append(line.strip())
    return grid


def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    def search_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return False
        return True

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if search_direction(r, c, dr, dc):
                    count += 1
                if search_direction(r, c, -dr, -dc):
                    count += 1

    return count


file_name = "d4p1-input.txt"
word_to_search = "XMAS"

grid = read_grid(file_name)

occurrences = count_word_occurrences(grid, word_to_search)

print(f"The word '{word_to_search}' occurs {occurrences} time(s) in the grid.")
