import sys,time
from collections import defaultdict

start=time.perf_counter()


def process_number(num):
    num = num.lstrip("0") or "0"

    if num == "0":
        yield "1"
    elif len(num) % 2 == 0:
        half_len = len(num) // 2
        first_half = int(num[:half_len])
        second_half = int(num[half_len:])
        yield str(first_half)
        yield str(second_half)
    else:
        yield str(int(num) * 2024)

def process_file(input_file, blinkNr):
    with open(input_file, 'r') as infile:
        numbers = infile.read().strip().split()

    number_counts = defaultdict(int)
    for num in numbers:
        number_counts[num] += 1

    for _ in range(blinkNr):
        next_counts = defaultdict(int)
        for num, count in number_counts.items():
            for new_num in process_number(num):
                next_counts[new_num] += count
        number_counts = next_counts

    total_count = sum(number_counts.values())
    print(f"Number of entries after processing: {total_count}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file> <blinkNr>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        blinkNr = int(sys.argv[2])
    except ValueError:
        print("Error: blinkNr must be an integer.")
        sys.exit(1)

    process_file(input_file, blinkNr)

end = time.perf_counter()

print(end - start)