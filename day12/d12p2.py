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

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if not is_valid_position(grid, nx, ny) or grid[nx][ny] != char:
                # Increment perimeter for each edge not shared with a matching neighbor
                tempPeriCtr += 1

    return tempAreaCtr * tempPeriCtr, tempPeriCtr

def calculate_total_lines(grid, visited, x, y, char):
    """
    Calculates the number of straight lines around a contiguous region.
    """
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = [(x, y)]
    region_edges = set()
    unique_edges = set()

    while stack:
        cx, cy = stack.pop()
        print(char,(cx, cy))

        if (cx, cy) in visited:
            continue

        visited.add((cx, cy))

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if not is_valid_position(grid, nx, ny) or grid[nx][ny] != char:
                # Add edge as a tuple to ensure no duplicates
                # print(region_edges)
                if (nx, ny) in unique_edges:
                    # print("NOPE")
                    unique_edges.add((nx,ny))
                elif (cx, cy) in unique_edges:
                    # print("nope")
                    unique_edges.add((cx, cy))
                else:
                    # print("here")
                    unique_edges.update([(cx, cy), (nx, ny)])

            elif (nx, ny) not in visited:
                stack.append((nx, ny))
    print("Char:", char, "Edges Cnt:", len(unique_edges), "Edges:", unique_edges)
    return len(unique_edges)

def calculate_final_sum(file_path):
    grid = get_grid(file_path)
    visited = set()
    final_sum = 0
    total_straight_lines = 0
    line_visited = set()

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                char = grid[x][y]
                product, _ = explore_region(grid, x, y, char, visited)
                final_sum += product

                # Calculate total lines
                if (x, y) not in line_visited:
                    total_straight_lines += calculate_total_lines(grid, line_visited, x, y, char)

    print("Total Straight Lines:", total_straight_lines)
    return final_sum

if __name__ == "__main__":
    file_path = 'd12-sample.txt'
    result = calculate_final_sum(file_path)
    print("Final Sum:", result)
