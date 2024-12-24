def print_triangle_for_loop(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        
        # Print numbers in increasing order
        for j in range(1, 2 * i):
            print(j, end=" ")
        
        # Move to the next line after each row
        print()

n = int(input("Enter the number of rows: "))
print_triangle_for_loop(n)
