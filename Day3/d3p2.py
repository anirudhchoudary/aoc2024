import re

def process_file_with_control_patterns(file_name):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    control_pattern = r"don't\(\)|do\(\)"
    
    combined_pattern = f"{mul_pattern}|{control_pattern}"
    
    total = 0
    consider_mul = True

    with open(file_name, 'r') as file:
        input_string = file.read()
    
    matches = re.finditer(combined_pattern, input_string)
    
    for match in matches:
        if match.group() == "don't()":
            consider_mul = False
        elif match.group() == "do()":
            consider_mul = True
        elif match.group(1) and match.group(2) and consider_mul:
            print(consider_mul)
            x = int(match.group(1))
            y = int(match.group(2))
            total += x * y
        elif match.group(1) and match.group(2) and not consider_mul:
            consider_mul = False
    
    return total

file_name = "d1p1-input.txt"

total_sum = process_file_with_control_patterns(file_name)

print("Total sum of multiplications:", total_sum)
