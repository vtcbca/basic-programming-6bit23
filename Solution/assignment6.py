def print_pattern_for_loop(rows):
    for i in range(1, rows + 1):
        print(" ".join(["*"] * i))

rows = int(input("Enter the number of rows: "))
print_pattern_for_loop(rows)
