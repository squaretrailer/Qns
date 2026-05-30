dic1 = {1:10, 2:20}; dic2 = {3:30, 4:40}; dic3 = {5:50, 6:60}

combined = {}
combined.update(dic1)
combined.update(dic2)
combined.update(dic3)

print(combined)