def is_prime_for_loop(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime_for_loop(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
