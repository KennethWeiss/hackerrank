#Give five integers in array
#Find max and min values that can be found by summing four values

def miniMaxSum(arr):
    min = arr[0]
    max = arr[0]
    sum = 0
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
        sum += i
    print(f"{sum-max} {sum-min}")