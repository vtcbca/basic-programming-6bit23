def factorial_for_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial_for_loop(number)}")
