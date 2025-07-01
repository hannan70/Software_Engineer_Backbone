def getRow(numRows):
    new_list = []
    for row in range(1, numRows+2):
        n = 1
        current_row = []
        for col in range(row):
            if row == 1 or col == 0:
                n = 1
            else:
                n = n * (row - col) // col
            current_row.append(n)
        new_list.append(current_row)
    return new_list[-1]


numRows = 1
print(getRow(numRows))





