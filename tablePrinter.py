#!/usr/bin/env python3 
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidths = [0] * len(data) # index [0] of the list * length of the (data) to be print out
    for j in range(len(data[0])): # finds a length of 4 items -- rows
        for i in range(len(data)): # finds a length of 3 items -- columns
            colWidths[i] = len((max(data[i], key=len))) # sets the column width to the maximum length of an item in the list
            a = data[i][j]
            print(a.rjust(colWidths[i]), end=" ")  # every time we print a column, we rjust it to the max width.
        print("\n")

printTable(tableData)


# for line 10 read more here ... https://developers.google.com/edu/python/sorting#custom-sorting-with-key=