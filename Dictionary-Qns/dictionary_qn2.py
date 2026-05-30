# QUESTION 2

data = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},
        {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

unique = set()
for d in data:
    for value in d.values():
        unique.add(value)
print("Unique Values:", unique)