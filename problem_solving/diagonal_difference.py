#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# I need to get the values of diagonals
# I need to loop through 1,1 2,2 3,3 so arr[i][i]
#That got left sum now for right
# [1][last], [2],[last-1]

def diagonalDifference(arr):
    # Write your code here
    left_sum = 0
    right_sum = 0
    length = len(arr)
    # print(f'the length is {length}')
    for value in range(length):
        end = length-1-value
        # print(f'Value: {value} and end:{end}')
        left_sum += arr[value][value]
        right_sum += arr[value][end]
    print(f'the length is {left_sum} and {right_sum}')
    if(left_sum>right_sum):
        return left_sum-right_sum
    elif(right_sum>left_sum):
        return right_sum-left_sum
    else:
        return 0

print(diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]))