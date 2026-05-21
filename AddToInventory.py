def AddToInventory(Inventory, addeditems):
    num = 0
    for i in addeditems :
        Inventory.setdefault(i, 0)
        n = Inventory.get(i, 0)
        Inventory[i] += 1
        
             
    return Inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',
              'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',
              'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = AddToInventory(inv, dragonLoot)
displayInventory(inv)

#for k,v in Inventory.items():



              
              
