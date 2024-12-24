def reverse_string_slicing(s):
    return s[::-1]

string = input("Enter a string: ")
reversed_string = reverse_string_slicing(string)
print(f"Reversed string: {reversed_string}")
