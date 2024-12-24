def print_pattern_for_loop(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        
        # Print increasing alphabets
        for j in range(1, i + 1):
            print(chr(64 + j), end=" ")
        
        # Print decreasing alphabets
        for j in range(i - 1, 0, -1):
            print(chr(64 + j), end=" ")
        
        # Move to the next line
        print()

n = int(input("Enter the number of rows: "))
print_pattern_for_loop(n)
