inventory = {"apple": 10, "banana": 5, "orange": 8}
item = input("Enter the item name: ")
if item in inventory:
    print(f"{item}: {inventory[item]}")
else:
    inventory[item] = 0
    print(f"{item}: {inventory[item]}") 