
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    
    n=0
    print("Inventory:")
    for i in inventory:
        n+=inventory[i]
        print(i,inventory[i])
    print("Total number of items:" + " " + str(n)) 

displayInventory(stuff)   
