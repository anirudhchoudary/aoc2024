from sympy import symbols, Eq, solve

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
        if ((solutions[A].is_integer and 0 < solutions[A] <= 100) and (solutions[B].is_integer and 0 < solutions[B] <= 100)):
            A_value = solutions[A]
            B_value = solutions[B]

            print(A_value, B_value)
            
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

slot_machines = read_slot_machine_data('d13-sample.txt')

print(solveLeastTokenCount(slot_machines))

