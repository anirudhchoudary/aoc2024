from sympy import symbols, Eq, solve, Mod, nsimplify
import math


def solveLeastTokenCount(slot_machines):

    totalTokenCount = 0

    for i, slot_machine in enumerate(slot_machines):
        A, B = symbols('A B')

        ax = slot_machine['ax']
        ay = slot_machine['ay']
        bx = slot_machine['bx']
        by = slot_machine['by']
        X = slot_machine['X'] + 10000000000000
        Y = slot_machine['Y'] + 10000000000000


        eq1 = Eq(ax * A + bx * B, X)
        eq2 = Eq(ay * A + by * B, Y)

        solutions = solve((eq1, eq2), (A, B))
        
        print(f"Slot Machine {i + 1}:", solutions)
        A_value = nsimplify(solutions[A])
        B_value = nsimplify(solutions[B])
        
        print(f"Slot Machine {i + 1}:", Mod(A_value,1), Mod(B_value,1))


        # if (A_value.is_integer and 0 < A_value) and (B_value.is_integer and 0 < B_value):
        if Mod(A_value,1) == 0 and Mod(B_value,1) == 0:
            A_value = int(round(A_value))
            B_value = int(round(B_value))

            print(f"Slot Machine {i + 1} Valid Values: A = {A_value}, B = {B_value}")

            result = A_value * 3 + B_value
            totalTokenCount += result

    return totalTokenCount


def read_slot_machine_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    slot_machines = []
    current_slot_machine = {}

    for line in lines:
        line = line.strip()
        if line.startswith('Button A'):
            parts = line.split(',')
            current_slot_machine['ax'] = int(parts[0].split('+')[1].strip())
            current_slot_machine['ay'] = int(parts[1].split('+')[1].strip())
        elif line.startswith('Button B'):
            parts = line.split(',')
            current_slot_machine['bx'] = int(parts[0].split('+')[1].strip())
            current_slot_machine['by'] = int(parts[1].split('+')[1].strip())
        elif line.startswith('Prize'):
            parts = line.split(',')
            current_slot_machine['X'] = int(parts[0].split('=')[1].strip())
            current_slot_machine['Y'] = int(parts[1].split('=')[1].strip())
        elif line == '':
            slot_machines.append(current_slot_machine)
            current_slot_machine = {}

    if current_slot_machine:
        slot_machines.append(current_slot_machine)

    return slot_machines

slot_machines = read_slot_machine_data('d13-input.txt')

print(solveLeastTokenCount(slot_machines))

