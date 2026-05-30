#Write a Python program to remove duplicate characters from a given string.
def remove_duplicates(s):
    seen = ""
    for ch in s:
        if ch not in seen:
            seen += ch
    return seen

print(remove_duplicates("programming"))  