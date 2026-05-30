#QUESTION 4

names = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = []
for name, code in zip(names, codes):
    result.append({"color_name": name, "color_code": code})
print(result)