def is_palindrome_slicing(s):
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome_slicing(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
