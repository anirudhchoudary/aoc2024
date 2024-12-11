import sys
import tempfile


def process_file(input_file, blinkNr):
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as temp_file:
        temp_file_name = temp_file.name

        with open(input_file, 'r') as infile:
            numbers = infile.read().strip().split()
            temp_file.write('\n'.join(numbers))

    while blinkNr > 0:

        with open(temp_file_name, 'r') as temp_file:
            numbers = temp_file.read().strip().split('\n')


        new_numbers = []

        for num in numbers:
            num = num.lstrip("0") or "0"

            if num == "0":
                new_numbers.append("1")
            elif len(num) % 2 == 0:
                half_len = len(num) // 2
                first_half = int(num[:half_len])
                second_half = int(num[half_len:])
                new_numbers.append(str(first_half))
                new_numbers.append(str(second_half))
            else:
                new_numbers.append(str(int(num) * 2024))

        with open(temp_file_name, 'w') as temp_file:
            temp_file.write('\n'.join(new_numbers))


        blinkNr -= 1

    with open(temp_file_name, 'r') as temp_file:
        final_numbers = temp_file.read().strip().split('\n')

    print(f"Number of entries in the temporary file: {len(final_numbers)}")

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
