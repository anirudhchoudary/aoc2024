from collections import deque

def read_file(file_path):
    with open(file_path, 'r') as file:
        coordinates = []
        for line in file:
            x, y = map(int, line.strip().split(','))
            coordinates.append((x, y))
    return coordinates

def create_grid(coordinates, G, byteCtr):
    grid = [['.' for _ in range(G+1)] for _ in range(G+1)]
    for array in grid:
        print(''.join(array))
    for i, (x, y) in enumerate(coordinates[:byteCtr]):
        if 0 <= x <= G and 0 <= y <= G:
            grid[y][x] = '#'
    print("============")
    for array in grid:
        print(''.join(array))
    return grid

def shortest_path(grid, G):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start, end = (0, 0), (G, G)
    queue = deque([(start[0], start[1], 0)])
    visited = set()

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == end:
            return steps

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= G and 0 <= ny <= G and grid[ny][nx] == '.' and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1))

    return -1

def main():
    file_path = 'd18-input.txt'
    G = 70
    byteCtr = 1024

    coordinates = read_file(file_path)
    grid = create_grid(coordinates, G, byteCtr)
    
    steps = shortest_path(grid, G)
    
    if steps != -1:
        print(f"Number of steps from (0, 0) to ({G-1}, {G-1}): {steps}")
    else:
        print("No valid path exists.")

if __name__ == "__main__":
    main()
