def formingMagicSquare(s):
    # Write your code here
    #first determine value of rows
    size = len(s)
    rows = []
    current_row = 0
    for i in range(size):
        print(f'index: {i} and size:{size}')
        for j in range(size):
            current_row += s[i][j]
        rows.append(current_row)
        current_row=0

    print(rows)

formingMagicSquare([[5,3,4],[1,5,8],[6,4,2]])