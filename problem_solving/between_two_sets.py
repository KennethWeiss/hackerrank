#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    factors = []
    count_between = 0

    for i in range(min(a), max(b)+1):
        is_in = True
        #a_val is the value in a
        for a_val in a:
            if i % a_val != 0:
                is_in = False
                print(f"{i} not multiple of a {a_val}")
                break
        for b_val in b:
            if is_in == False:
                break
            if b_val % i != 0:
                is_in = False
                print(f"{i} not factor of b {b_val}")
                break
        if is_in:
            count_between += 1
            print(f"{i} is in between count between = {count_between}")
            print("")
    print(f"{count_between} is the coutn between")
    return count_between

        # for j in range(1, i+1):
        #     if(i%j==0 and j not in factors):
        #         factors.append(j)
        # print(f"Value in b: {i}")

    print(factors)


a = [1]
b = [100]

print(getTotalX(a,b))