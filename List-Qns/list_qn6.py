# QUESTION 6

nums = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
rounded = [round(n) for n in nums]

print("Minimum value:", min(rounded))  
print("Maximum value:", max(rounded))   

times5 = [n * 5 for n in rounded]
unique_sorted = sorted(set(times5))
print("Result:", " ".join(str(n) for n in unique_sorted))