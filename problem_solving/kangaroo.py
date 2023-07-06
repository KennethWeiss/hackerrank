#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1 kang1 initial location
#  2. INTEGER v1 kang1 velocity
#  3. INTEGER x2 kang2 initial location
#  4. INTEGER v2 kang2 velocity
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    kang1 = x1+v1
    kang2 = x2+v2
    dist = x2-x1
    vel = v1 - v2
    if((x1>x2 and v1>v2) or (x1<x2 and v1<v2) or (x1!=x2 and v1==v2)):
        return "NO"
    elif(dist%vel != 0):
        return "NO"
    else:
        return "YES"