def is_safe_sequence(seq):
    directions = []
    
    for i in range(1, len(seq)):
        diff = abs(seq[i] - seq[i - 1])
        if diff < 1 or diff > 3:
            return False
        directions.append(seq[i] - seq[i - 1])

    directionPlusCount = sum(1 for d in directions if d >= 0)
    return directionPlusCount == 0 or directionPlusCount == len(directions)

def count_safe_levels_with_removals(file_name):
    safeLevelCtr = 0

    with open(file_name, 'r') as file:
        for line in file:
            levels = line.strip().split()
            report = list(map(int, levels))

            if is_safe_sequence(report):
                safeLevelCtr += 1
            else:
                for i in range(len(report)):
                    dampenedReport = report[:i] + report[i + 1:]
                    if is_safe_sequence(dampenedReport):
                        safeLevelCtr += 1
                        break

    return safeLevelCtr

file_name = 'd2p1-input.txt'
safe_levels = count_safe_levels_with_removals(file_name)
print("Final value of safeLevelCtr:", safe_levels)
