# Given an array of integers, 
# calculate the ratios of its elements that are 
# positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with places after the decimal.
#example arr[1,1,0,-1,-1]
#0.400000
#0.200000
#0.400000

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i<0:
            pos+=1
        elif i>0:
            neg+=1
        else:
            zero += 1
    print('%.6f' % (pos/len(arr)))
    print('%.6f' % (neg/len(arr)))
    print('%.6f' % (zero/len(arr)))
    return arr

plusMinus([1,1,0,-1,-1])