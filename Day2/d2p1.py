safeLevelCtr = 0


with open('d2p1-input.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))

        is_safe = True
        for i in range(len(numbers) - 1):
            diff = abs(numbers[i] - numbers[i + 1])
            if (diff > 3 or diff < 1) or (numbers[i] < numbers[i + 1] and numbers[i + 1] - numbers[i] > 3):
                is_safe = False
                break

        
        if is_safe and (numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)):
            safeLevelCtr += 1


print("Final value of safeLevelCtr:", safeLevelCtr)
