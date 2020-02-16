def displayInventory(inventory):
    
    n=0
    print("Inventory:")
    for i in inventory:
        n+=inventory[i]
        print(i,inventory[i])
    print("Total number of items:" + " " + str(n)) 
   


def addToInventory(inventory, addedItems):
    for new in addedItems:
        if new in inventory:
            inventory[new]+=1
        else:
            inventory[new]=1
    return inventory
        
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
