# List comprehensions
#[expression for if]


def list_comp(x,y,z,n):
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k) != n])

list_comp(1,1,1,2)