# inventory.py
import commaCode

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory: ')
    total = 0
    for item, amount in inventory.items():
        total += amount
        print(str(amount) + ' ' + item)
    print('Total number of items: ' + str(total))

def updateInventory(inventory, lootDrops):
    for loot in lootDrops:
        if loot in inventory.keys():
            inventory[loot] += 1
        else:
            inventory[loot] = 1

def newLine():
    print('')

def fakeRPG():
    displayInventory(inventory)
    newLine()
    print('hero defeats dragon...')
    newLine()
    print('loot dropped : ', end='')
    commaCode.commaCode(dragonLoot)
    newLine()
    print('updating inventory...')
    newLine()
    updateInventory(inventory, dragonLoot)
    displayInventory(inventory)

fakeRPG()
