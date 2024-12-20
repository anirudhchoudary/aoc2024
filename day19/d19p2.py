def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    tPattern = []
    oDesigns = []

    tPattern = [pattern.strip() for pattern in lines[0].split(',')]

    blank_index = lines.index('\n')
    oDesigns = [line.strip() for line in lines[blank_index + 1:] if line.strip()]

    return tPattern, oDesigns

from functools import lru_cache

def ai_count_ways_to_form_design(tPattern, oDesign):
    """Counts the number of ways oDesign can be formed using combinations of strings in tPattern, with caching."""
    tPattern_set = tuple(tPattern)  # Convert to immutable type for caching

    @lru_cache(None)
    def backtrack(remaining):
        if not remaining:
            return 1  # Successfully constructed oDesign
        count = 0
        for word in tPattern_set:
            if remaining.startswith(word):  # Check if current word can form the prefix
                count += backtrack(remaining[len(word):])  # Continue with the remaining part
        return count

    return backtrack(oDesign)


def count_ways_to_form_design(tPattern, oDesign):
    def backtrack(remaining):
        if not remaining:
            return 1
        count = 0
        for word in tPattern:
            if remaining.startswith(word):
                count += backtrack(remaining[len(word):])
        return count

    return backtrack(oDesign)

def count_total_design_matches(file_path):
    tPattern, oDesigns = read_file(file_path)
    total_count = 0

    for oDesign in oDesigns:
        ways = ai_count_ways_to_form_design(tPattern, oDesign)
        # print(f"oDesign '{oDesign}' can be formed in {ways} ways.")
        total_count += ways

    print(f"Total number of ways all oDesigns can be formed: {total_count}")
    return total_count

def main():
    file_path = 'd19-input.txt'
    count_total_design_matches(file_path)

if __name__ == "__main__":
    main()
