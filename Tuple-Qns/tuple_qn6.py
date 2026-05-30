
data = ((10,10,10,12),(30,45,56,45),(81,80,39,32),(1,2,3,4))
print([sum(col)/len(col) for col in zip(*data)])

data2 = ((1,1,-5),(30,-15,56),(81,-60,-39),(-10,2,3))
print([sum(col)/len(col) for col in zip(*data2)])