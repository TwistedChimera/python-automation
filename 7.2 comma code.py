def commaCode(itemList):
    if (len(itemList) > 1):
        itemList.insert(-1, 'and')
    for index in range(len(itemList)):
        if(index < len(itemList) - 2):
            print(itemList[index], end=', ')
        else:
            print(itemList[index], end=' ')
    print('')

spam = ['apples', 'bananas', 'tofu', 'cats'] * 5
bacon = ['cookies']

commaCode(spam)
commaCode(bacon)
