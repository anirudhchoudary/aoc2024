def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    tPattern = []
    oDesigns = []

    tPattern = [pattern.strip() for pattern in lines[0].split(',')]

    blank_index = lines.index('\n')
    oDesigns = [line.strip() for line in lines[blank_index + 1:] if line.strip()]

    return tPattern, oDesigns

def count_design_matches(file_path):
    tPattern, oDesigns = read_file(file_path)
    oDctr = 0

    for oDesign in oDesigns:
        if can_form_design(tPattern, oDesign):
            oDctr += 1
            # print(oDctr)

    print(f"Number of matching oDesigns: {oDctr}")
    return oDctr

def can_form_design(tPattern, oDesign):
    def backtrack(remaining, used):
        if not remaining:
            return True
        
        for word in tPattern:
            if remaining.startswith(word):
                if backtrack(remaining[len(word):], used + [word]):
                    return True
        
        return False

    return backtrack(oDesign, [])


def main():
    file_path = 'd19-input.txt'
    count_design_matches(file_path)

if __name__ == "__main__":
    main()
