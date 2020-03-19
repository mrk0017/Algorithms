def minOperation(A):
    i=1
    count=0
    B=[]
    B.append(A[0])
    print(B)
    while i<len(A):
        lcount=0
        rcount=0
        for j in B:
            if j<A[i]:
                lcount=lcount+1
        rcount=len(B)-lcount
        if lcount<rcount:
            count=(lcount*2)+1
        else:
            count=(rcount*2)+1
        B.append(A[i])
        B.sort()
        print("lcount: ",lcount,"rcount: ",rcount, "count: ",count)
        print(B)
        i=i+1
    return count

A=[2,4,7,10,11,3,6,5]
print(minOperation(A))
