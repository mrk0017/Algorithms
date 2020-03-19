def MSA(A,n):
    if n==0:
        return 1
    else:
        num=MSA(A,n-1)
        if A[n-1]!=A[n]:
            num=num+1
        return num

def DE(A,n):
    if n==0:
        print(A[n])
    else:
        DE(A,n-1)
        print(A[n])


if __name__ == "__main__":
    A=[1,2,2,3,4,4,5,6,7,8,10]
    #print(MSA(A,len(A)-1))
    DE(A,len(A)-1)