# Write a Python program to delete all occurrences of a specified character in a given string.
#Sample Output:
#Original string:
#Delete all occurrences of a specified character in a given string
#Modified string:
#Delete ll occurrences of specified chrcter in given string


def delete_char(s, c):
    return s.replace(c, "")

text = "Delete all occurrences of a specified character in a given string"
print(delete_char(text, "a"))