# 1. Length of a set
s = {1, 2, 3, 4}
print(len(s))          

# 2. Add member(s)
s.add(5)               
s.update([6, 7])        
print(s)                 

# 3. Remove item(s)
s.discard(7)            
print(s)                

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 4. Intersection — items in BOTH
print(a & b)           

# 5. Union — items in EITHER
print(a | b)           

# 6. Difference — in a but NOT b
print(a - b)           

# 7. Max and min
print(max(a), min(a))