# Write a Python function to get a string made of the first three characters of a sepcified string. If the length of the string is less than 3, return the original string.
# Sample function and result:
# first_three('Python') -> 'Pyt'
# first_three('ipy') -> 'ipy'

def first_three(s):
    if len(s) < 3:
        return s
    return s[:3]

# Test the function
print(first_three('Python'))  # Output: 'Pyt'
print(first_three('ipy'))     # Output: 'ipy'