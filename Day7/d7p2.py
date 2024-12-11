def check_recursive(valNums, target):
    if len(valNums) == 1:
        return valNums[0] == target

    first, second = valNums[0], valNums[1]

    if check_recursive([first + second] + valNums[2:], target):
        return True

    if check_recursive([first * second] + valNums[2:], target):
        return True
    
    if check_recursive([int(str(first) + str(second))] + valNums[2:], target):
        return True

    return False

finalSum = 0
myList = []

with open('d7-input.txt') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    testVal_str, valNums_str = line.split(": ")
    testVal = int(testVal_str)
    valNums = [int(x) for x in valNums_str.split()]
    myList.append([testVal] + valNums)

for entry in myList:
    testVal = entry[0]
    valNums = entry[1:]

    if len(valNums) == 1:
        if valNums[0] != testVal:
            continue

    elif len(valNums) == 2:
        if valNums[0] + valNums[1] == testVal or valNums[0] * valNums[1] == testVal or int(str(valNums[0]) + str(valNums[1])) == testVal:
            finalSum += testVal

    else:
        if check_recursive(valNums, testVal):
            finalSum += testVal

print("Final Sum:", finalSum)
