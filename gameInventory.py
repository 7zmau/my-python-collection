def displayInventory(inventory):
    print("Inventory Items:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total no. of items:", item_total)

#Following section I wrote on my own, so cheers!!
def addtoInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i, 1)
    return inventory


inv = {'gold coin' : 42, 'rope' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addtoInventory(inv, dragonLoot)
displayInventory(inv)
