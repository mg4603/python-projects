tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def print_table(tableData):
    colWidths = [0] * len(tableData)
    for col_no in range(len(tableData)):
        colWidths[col_no] = max([len(word) for word in tableData[col_no]])
    
    for row_no in range(len(tableData[0])):
        for col_no in range(len(tableData)):
            print(tableData[col_no][row_no].rjust(colWidths[col_no], " "), end = " ")
        print()

print_table(tableData)