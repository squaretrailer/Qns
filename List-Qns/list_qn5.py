# QUESTION 5

def move_zeros(nums):
    non_zeros = [n for n in nums if n != 0]
    zeros = [n for n in nums if n == 0]
    return non_zeros + zeros

print(move_zeros([3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]))