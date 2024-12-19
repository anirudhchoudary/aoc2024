def read_file(file_path):
    with open(file_path, 'r') as file:
        regA = regB = regC = 0
        programArr = []

        for line in file:
            if "Register A:" in line:
                regA = int(line.split("Register A:")[1].strip())
            elif "Register B:" in line:
                regB = int(line.split("Register B:")[1].strip())
            elif "Register C:" in line:
                regC = int(line.split("Register C:")[1].strip())
            elif "Program:" in line:
                programArr = list(map(int, line.split("Program:")[1].strip().split(',')))

    return regA, regB, regC, programArr


def process_program(regA, regB, regC, programArr):
    results = []
    i = 0
    program_len = len(programArr)

    lOperands = {i: i for i in range(8)}

    def get_cOperand(operand, regA, regB, regC):
        cOperands = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: regA,
            5: regB,
            6: regC
        }
        return cOperands.get(operand, 0)

    while i < program_len:
        opcode = programArr[i]
        operand = programArr[i + 1] if i + 1 < program_len else 0

        lOperand = lOperands.get(operand, 0)
        cOperand = get_cOperand(operand, regA, regB, regC)

        # Perform operations based on opcode
        if opcode == 0:
            regA = regA // (2 ** cOperand)
        elif opcode == 1:
            regB = regB ^ lOperand
        elif opcode == 2:
            regB = cOperand % 8
        elif opcode == 3:
            if regA != 0:
                i = lOperand
                continue
        elif opcode == 4:
            regB = regB ^ regC
        elif opcode == 5:
            result = cOperand % 8
            results.append(result)
        elif opcode == 6:
            regB = regA // (2 ** cOperand)
        elif opcode == 7:
            regC = regA // (2 ** cOperand)

        i += 2

    return results


def main():
    file_path = 'd17-input.txt'
    regA, regB, regC, programArr = read_file(file_path)
    results = process_program(regA, regB, regC, programArr)
    print(",".join(map(str, results)))


if __name__ == "__main__":
    main()
