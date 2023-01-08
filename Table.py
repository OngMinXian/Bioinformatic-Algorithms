def printTable(rowLabels, colLabels, data, margin_for_printing):

    if len(rowLabels) != len(data) or len(colLabels) != len(data[0]):
        print('table not possible')
        return
    
    margin = margin_for_printing
    remove_left_margin = max(map(lambda x: len(x), rowLabels)) + 1

    topRow = ' ' * (remove_left_margin)
    for i in colLabels:
        topRow += (margin-len(i))*' ' + i
    print(topRow)

    for i in range(len(rowLabels)):
        row = ''
        row += (remove_left_margin-len(rowLabels[i]))*' ' + rowLabels[i]
        for j in range(len(colLabels)):
            value = str(data[i][j])
            row += (margin-len(value))*' ' + value
        print(row)