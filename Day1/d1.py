list1 = []
list2 = []

pairDist = 0
simScore = 0

with open('d1p1-input.txt', 'r') as file:
    for line in file:
        numbers = line.strip().split()
        if len(numbers) == 2:
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))


list1.sort()
list2.sort()

for num1, num2 in zip(list1, list2):
    pairDist += abs(num1 - num2)

for num1 in list1:
    appearCtr = list2.count(num1)
    simScore += num1 * appearCtr

print("Final value of pairDist:", pairDist)
print("Final value of simScore:", simScore)
