#Write a Python program that counts the number of leap years within the range of years. Ranges of years should be accepted as strings.
#Sample Data:
#("1981-1991") -> 2
#("2000-2020") -> 6

def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def count_leap(span):
    start, end = span.split("-")
    count = 0
    for y in range(int(start), int(end) + 1):
        if is_leap(y):
            count += 1
    return count

print(count_leap("1981-1991")) 
print(count_leap("2000-2020"))  