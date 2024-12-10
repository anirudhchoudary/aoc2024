def read_input_file(file_name):
    rules = []
    updates = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                rules.append(tuple(map(int, line.split("|"))))
            elif "," in line:
                updates.append(list(map(int, line.split(","))))
    return rules, updates


def check_update_sequence(update, rules):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[i], update[j]) not in rules:
                return False
    return True


def is_correct_order(update, rules):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in rules:
                return False
    return True


def fix_update_sequence(update, rules):
    update = update[:]
    n = len(update)
    for i in range(n):
        for j in range(i + 1, n):
            if (update[j], update[i]) in rules:
                update[i], update[j] = update[j], update[i]

    if check_update_sequence(update, rules) and is_correct_order(update, rules):
        return update
    else:
        return None


def process_updates(file_name):
    rules, updates = read_input_file(file_name)

    valid_updates = []
    incorrect_updates = []
    fixed_updates = []

    for update in updates:
        if check_update_sequence(update, rules) and is_correct_order(update, rules):
            valid_updates.append(update)
        else:
            incorrect_updates.append(update)
            fixed_update = fix_update_sequence(update, rules)
            if fixed_update:
                fixed_updates.append(fixed_update)

    
    middle_sum_valid = 0
    for update in valid_updates:
        middle_index = len(update) // 2
        middle_sum_valid += update[middle_index]

    
    middle_sum_fixed = 0
    for update in fixed_updates:
        middle_index = len(update) // 2
        middle_sum_fixed += update[middle_index]

    return middle_sum_valid, middle_sum_fixed, incorrect_updates



file_name = "d5p1-input.txt"


middle_sum_valid, middle_sum_fixed, incorrect_updates = process_updates(file_name)


print(f"middle numbers sum in valid updates: {middle_sum_valid}")
print(f"middle numbers sum in corrected update: {middle_sum_fixed}")

