# This is a staircase of size n=4 :

#    # 3space 1#
#   ## 2space 2#
#  ### 1space 3#
# #### 0space 4#

def staircase(n):
    for i in range(n):
        spaces = ' ' * (n-i-1)
        hashes = '#' * (i+1)
        print(spaces+hashes)
staircase(4)