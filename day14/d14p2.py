from collections import deque

def read_robot_data(file_path):
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                p_values = list(map(int, parts[0].split('=')[1].split(',')))
                v_values = list(map(int, parts[1].split('=')[1].split(',')))
                robots.append({
                    'xpos': p_values[0],
                    'ypos': p_values[1],
                    'xvel': v_values[0],
                    'yvel': v_values[1],
                })
    return robots

def move_robot(robot, xLimit, yLimit):
    x_moves = abs(robot['xvel'])
    direction_x = 1 if robot['xvel'] > 0 else -1
    while x_moves > 0:
        if 0 <= (robot['xpos'] + direction_x) < xLimit:
            robot['xpos'] += direction_x
            x_moves -= 1
        else:
            robot['xpos'] = 0 if direction_x > 0 else (xLimit - 1)
            x_moves -= 1

    y_moves = abs(robot['yvel'])
    direction_y = 1 if robot['yvel'] > 0 else -1
    while y_moves > 0:
        if 0 <= (robot['ypos'] + direction_y) < yLimit:
            robot['ypos'] += direction_y
            y_moves -= 1
        else:
            robot['ypos'] = 0 if direction_y > 0 else (yLimit - 1)
            y_moves -= 1

def detect_connected_components(grid, X, Y):
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen = set()
    components = 0

    for y in range(Y):
        for x in range(X):
            if grid[y][x] == '#' and (x, y) not in seen:
                components += 1
                queue = deque([(x, y)])
                while queue:
                    cx, cy = queue.popleft()
                    if (cx, cy) in seen:
                        continue
                    seen.add((cx, cy))
                    for dx, dy in DIRS:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < X and 0 <= ny < Y and grid[ny][nx] == '#':
                            queue.append((nx, ny))
    return components

def check_christmas_tree_shape(robot_positions, X, Y):
    grid = [['.' for _ in range(X)] for _ in range(Y)]
    for x, y in robot_positions:
        grid[y][x] = '#'
    components = detect_connected_components(grid, X, Y)
    return components <= 200

def process_robots(file_path):
    xLimit, yLimit = 101, 103
    robots = read_robot_data(file_path)
    iterations = 0

    while iterations < 10000:
        iterations += 1
        for robot in robots:
            move_robot(robot, xLimit, yLimit)

        robot_positions = {(robot['xpos'], robot['ypos']) for robot in robots}
        if check_christmas_tree_shape(robot_positions, xLimit, yLimit):
            print(f"Christmas tree formation achieved in {iterations} iterations")
            print("Final Layout:")
            grid = [['.' for _ in range(xLimit)] for _ in range(yLimit)]
            for x, y in robot_positions:
                grid[y][x] = '#'
            for row in grid:
                print(''.join(row))
            return iterations

    print("Failed to achieve Christmas tree formation within the iteration limit")
    return -1

if __name__ == "__main__":
    file_path = 'd14-input.txt'
    process_robots(file_path)
