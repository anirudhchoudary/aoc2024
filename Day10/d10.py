def read_grid(file_name):
    grid = {}
    with open(file_name, 'r') as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                grid[(x, y)] = int(char)
    return grid

def find_trailheads(grid):
    return [position for position, value in grid.items() if value == 0]

def explore_trail(grid, trailhead, count_distinct_paths=False):
    score = 0
    queue = [trailhead]
    encountered_positions = set()
    while queue:
        position = queue.pop(0)
        if position in encountered_positions and not count_distinct_paths:
            continue
        if not count_distinct_paths:
            encountered_positions.add(position)
        elevation = grid[position]
        if elevation == 9:
            score += 1
            continue
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        surrounding_positions = [
            (position[0] + dx, position[1] + dy)
            for dx, dy in directions
            if (position[0] + dx, position[1] + dy) in grid and grid[(position[0] + dx, position[1] + dy)] == elevation + 1
        ]
        queue.extend(surrounding_positions)
    return score

def simulate(file_name):
    grid = read_grid(file_name)
    trailheads = find_trailheads(grid)
    part1_score = sum(explore_trail(grid, trailhead) for trailhead in trailheads)
    part2_score = sum(explore_trail(grid, trailhead, count_distinct_paths=True) for trailhead in trailheads)
    print(f"Part 1: {part1_score}")
    print(f"Part 2: {part2_score}")

file_name = "d10p1-input.txt"
simulate(file_name)
