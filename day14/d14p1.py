# Sample Tile size
#   xlimit = 11, ylimit = 7
# Actual Tile size
#   xlimit = 101, ylimit = 103

# midXlimit = (xlimit // 2)
# midYlimit = (ylimit // 2)

# if 0 <= xpos < midXlimit and 0 <= ypos < midYlimit, then increment a counter q1RobotCtr.
# if midXlimit < xpos < xLimit and 0 <= ypos < midYlimit, then increment a counter q2RobotCtr
# if 0 <= xpos < midXlimit and midYlimit < ypos < yLimit, then increment a counter q3RobotCtr
# if midXlimit < xpos <= xLimit and midYlimit < ypos <= yLimit, then increment a counter q4RobotCtr

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

def process_robots(file_path):
    # xLimit, yLimit = 11, 7
    xLimit, yLimit = 101, 103
    midXlimit = (xLimit // 2)
    midYlimit = (yLimit // 2)


    q1RobotCtr = 0
    q2RobotCtr = 0
    q3RobotCtr = 0
    q4RobotCtr = 0

    robots = read_robot_data(file_path)

    for robot in robots:
        for _ in range(100):
            move_robot(robot, xLimit, yLimit)

        xpos = robot['xpos']
        ypos = robot['ypos']

        # print(xpos,ypos)

        if xpos == midXlimit or ypos == midYlimit:
            continue

        if 0 <= xpos < midXlimit and 0 <= ypos < midYlimit:
            q1RobotCtr += 1
        elif midXlimit < xpos < xLimit and 0 <= ypos < midYlimit:
            q2RobotCtr += 1
        elif 0 <= xpos < midXlimit and midYlimit < ypos < yLimit:
            q3RobotCtr += 1
        elif midXlimit < xpos < xLimit and midYlimit < ypos < yLimit:
            q4RobotCtr += 1
    print(q1RobotCtr, q2RobotCtr, q3RobotCtr, q4RobotCtr)
    product = q1RobotCtr * q2RobotCtr * q3RobotCtr * q4RobotCtr
    print(f"Product: {product}")
    return product

if __name__ == "__main__":
    file_path = 'd14-input.txt'
    process_robots(file_path)
