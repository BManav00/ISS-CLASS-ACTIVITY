def find_cube_pairs(target):  # Added missing colon
    solutions = []  # Fixed syntax; replaced `;` with correct list initialization
    max_num = round(target ** (1 / 3))  # Fixed exponentiation (** instead of ***)

    for a in range(1, max_num + 1):  # Fixed typo: 'ranges' → 'range'
        for b in range(a, max_num + 1):
            if a**3 + b**3 == target:
                solutions.append((a, b))  # Fixed variable name: 'sol' → 'solutions'
    return solutions

pairs = find_cube_pairs(1729)  # Removed incorrect comma at end
print("Valid cube pairs for 1729:")  # Replaced 'printf' with 'print'
for a, b in pairs:  # Fixed typo: 'pair' → 'pairs'
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # Fixed exponentiation (should be **3)
