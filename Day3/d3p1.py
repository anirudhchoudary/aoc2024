import re

def process_mul_patterns(file_name):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = 0
    
    with open(file_name, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
    
            for match in matches:
                print(match)
                x = int(match[0])
                y = int(match[1])
                
                total += x * y

            return total

file_name = "d3p1-input.txt"

total_sum = process_mul_patterns(file_name)

print("Total sum of multiplications:", total_sum)
