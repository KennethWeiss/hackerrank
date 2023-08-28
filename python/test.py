def this_try(n):
    if(n%2 != 0):
        print("Entered if")
        print("Weird")
    else:
        print("Entered else")
        if(n>20):
            print("Not Weird")
        elif(n>=6):
            print("Weird")
        print("Weird")


def square(n):
    for i in range(0,n):
        if(i<n):
            print(i*i)

def listNums(n):
    strList = ""
    for i in range(1,n+1):
        strList += str(i)
    print(strList)
    

listNums(5)