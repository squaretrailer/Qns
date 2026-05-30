# QUESTION 3

def concat_range(items, n):
    result = []
    for i in range(1, n + 1):
        for item in items:
            result.append(item + str(i))
    return result

print(concat_range(['p', 'q'], 5))