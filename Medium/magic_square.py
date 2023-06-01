def formingMagicSquare(s):
    # Write your code here
    #first determine value of rows
    size = len(s)
    rows = []
    diagonals = []
    columns = []
    current_row = 0
    current_col = 0
    left_diag = 0
    right_diag = 0
    for i in range(size):
        end = size-1-i
        print(f'index: {i} and size:{size}')
        left_diag += s[i][i]
        right_diag += s[i][end]
        for j in range(size):
            current_row += s[i][j]
            current_col += s[j][i]
        columns.append(current_col)
        rows.append(current_row)
        current_row=0
        current_col=0
    counts = []
    for i in rows:
        counts.append(i)
    for i in columns:
        counts.append(i)
    for i in diagonals:
        counts.append(i)
    print(f'All: {counts}')
    print(f"most frequent is {mode(counts)}")
    print(f'Rows: {rows} Columns: {columns} Left:{left_diag} Right:{right_diag}')

formingMagicSquare([[5,3,4],[1,5,8],[6,4,2]])