def formingMagicSquare(s):
    # Write your code here
    #first determine value of rows
    size = len(s)
    rows = []
    diagonals = []
    columns = []
    current_row = 0
    current_col = 0
    for i in range(size):
        print(f'index: {i} and size:{size}')
        for j in range(size):
            current_row += s[i][j]
            current_col += s[j][i]
        columns.append(current_col)
        rows.append(current_row)
        current_row=0
        current_col=0

    print(f'Rows: {rows} Columns: {columns}')

formingMagicSquare([[5,3,4],[1,5,8],[6,4,2]])