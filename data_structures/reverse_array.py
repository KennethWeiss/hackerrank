def reverse_array(a):
    reverse = []
    for i in range(len(a)-1, -1, -1):
        reverse.append(a[i])
    print(reverse)

first = [1,2,3,4,5]
second = [2,4,6,8,10]

reverse_array(first)
reverse_array(second)