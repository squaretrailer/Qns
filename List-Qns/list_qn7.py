# QUESTION 7

def count_lists(data):
    count = 0
    for item in data:
        if isinstance(item, list):
            count += 1
    return count

print(count_lists([[1,3],[5,7],[9,11],[13,15,17]]))     
print(count_lists([[2,4],[[6,8],[4,5,8]],[10,12,14]]))