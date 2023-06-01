#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# I need to get the values of diagonals
# I need to loop through 1,1 2,2 3,3 so arr[i][i]

def diagonalDifference(arr):
    # Write your code here
    left_sum = 0
    length = len(arr)
    # print(f'the length is {length}')
    for value in range(length):
        left_sum += arr[value][value]
    return left_sum

print(diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]))