fruits=["Apple","Banana","Mango"]
vegetables=["Carrot","Tomato","Cucumber"]
beverages=["Juice","Coffee","Tea"]
fruits.append("Orange")
vegetables.insert(1,"Broccoli")
beverages.pop()
inventory=[fruits,vegetables,beverages]
print("First two fruits:",fruits[:2])
print("Last vegetable:",vegetables[-1])
fruit_lengths=[len(item) for item in fruits]
print("Lengths of fruits:",fruit_lengths)
has_water="Water" in beverages
print("Is 'Water' in beverages?:",has_water)
first_items=(fruits[0],vegetables[0],beverages[0])
print("Tuple of first items:",first_items)