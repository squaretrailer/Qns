
items = {'item1':45.50, 'item2':35, 'item3':41.30, 'item4':55, 'item5':24}

top3 = sorted(items.items(), key=lambda x: x[1], reverse=True)[:3]
for name, price in top3:
    print(name, price)