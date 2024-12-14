def get_grid(file_path):
    grid = []
    with open(file_path, 'r') as f:
        for line in f:
            grid.append(list(line.rstrip()))
    return grid

def is_valid_position(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def explore_region(grid, x, y, char, visited):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = [(x, y)]
    tempAreaCtr = 0
    tempPeriCtr = 0

    while stack:
        cx, cy = stack.pop()

        if (cx, cy) in visited:
            continue

        visited.add((cx, cy))
        tempAreaCtr += 1

        matches = 0

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if is_valid_position(grid, nx, ny):
                if grid[nx][ny] == char:
                    matches += 1
                    if (nx, ny) not in visited:
                        stack.append((nx, ny))

        tempPeriCtr += (4 - matches)
        # print(char, tempPeriCtr)

    # print("Char:", char, "Area:", tempAreaCtr, "Perimeter:", tempPeriCtr, "Product:", tempAreaCtr * tempPeriCtr)
    return tempAreaCtr * tempPeriCtr

def calculate_final_sum(file_path):
    grid = get_grid(file_path)
    visited = set()
    final_sum = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                char = grid[x][y]
                product = explore_region(grid, x, y, char, visited)
                final_sum += product

    return final_sum

if __name__ == "__main__":
    file_path = 'd12-input.txt'
    result = calculate_final_sum(file_path)
    print("Final Sum:", result)
