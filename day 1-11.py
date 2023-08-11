from itertools import permutations


def solve_cryptarithmetic(puzzle):

    unique_letters = set(''.join(puzzle))
    letters = ''.join(unique_letters)
    

    for perm in permutations('0123456789', len(unique_letters)):
        digit_map = dict(zip(unique_letters, perm))
        

        if any(digit_map[word[0]] == '0' for word in puzzle):
            continue

        expression = ' '.join(''.join(digit_map[char] for char in word) for word in puzzle)
        if eval("expression"):
            return digit_map
    
    return None


puzzle = ["send", "more", "money"]
solution = solve_cryptarithmetic(puzzle)

if solution:
    print("Solution exists:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution exists.")
