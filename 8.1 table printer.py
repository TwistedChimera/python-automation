# to avoid confusion,
# each list will be printed in column form
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
# column view
# [list 1] [list 2] [list 3]
# [list 1] [list 2] [list 3]
# . . .


# Find longest string for each list to use as padding
def findLongest(table):
    # find longest string from each list
    colWidths = [0] * len(tableData) # [0, 0, 0]
    for row in range(len(table)):
        for column in range(len(table[row])):
            if len(table[row][column]) > colWidths[row]:
                colWidths[row] = len(table[row][column])
    return colWidths

# Print table
def printTable(table):
    padding = findLongest(table)
    # list
    row = len(table)
    # element
    column = len(table[0]) #assumes uniform length for all lists
    # my brain @.@
    # increment element index after cycling through each list
    for i in range(column): # index of element
        for j in range(row): # index of list
            # prints same indexed element from each list
            # padding matched for each list cycled
            print(table[j][i].rjust(padding[j]), end=' ')
        print('') # newline

printTable(tableData)

# NOTE: This is some mind fuckery shit.
