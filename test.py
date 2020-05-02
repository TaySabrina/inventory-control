from time import sleep
print('\033[34m === INVENTORY CONTROL ===\033[m')
items = list()
products = ' '
while True:
    ask = ' '
    products = str(input('Write the name of the item to add to inventory: '))
    items.append(products)
    ask = str(input('Do you want to add more? [S/N] ')).upper()[0]
    if ask == 'N':
        break
print(f'Added items: \033[32m{items}\033[m')
sleep(1)
print('Shutting down... ')
sleep(1)
print('\033[31mTHANK YOU!\033[m')