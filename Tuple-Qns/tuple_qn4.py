def tuple_to_int(t):
    return int("".join(str(n) for n in t))

print(tuple_to_int((1,2,3)))             
print(tuple_to_int((10,20,40,5,70)))    