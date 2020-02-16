tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)

def printTable(x):
    for i in range(len(x)):
        c=[0]*len(x[i])
        for j in range(len(x[i])):
            c.append(len(x[i][j]))
        colWidths[i]=max(c)
    l = max(colWidths)

    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j].rjust(l),end="")
        print("")

printTable(tableData)
