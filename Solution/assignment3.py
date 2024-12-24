def fibonacci_for_loop(terms):
    fib_sequence = [0, 1]
    for i in range(2, terms):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence

terms = int(input("Enter the number of terms: "))
fib_seq = fibonacci_for_loop(terms)
print(f"Fibonacci sequence with {terms} terms: {fib_seq}")
