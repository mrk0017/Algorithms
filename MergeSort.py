def no_inversions(A):
    l=0
    r=len(A)-1
    if l==r:
        return 0
    else:
        mid=int((l+r)/2)
        B=A[l:mid+1]
        C=A[mid+1:]
        linversion=no_inversions(B)
        rinversion=no_inversions(C)
        print("linv ", linversion)
        print("rinv ", rinversion)

        count=0
        a=0
        b=0
        c=0
        while b<len(B) and c<len(C):
            print("B: ",B)
            print("C: ",C)
            if B[b]<=C[c]:
                A[a]=B[b]
                a=a+1
                b=b+1
            else:
                A[a]=C[c]
                a=a+1
                c=c+1
                count=count+len(B)-b
                print("count inc count",count, A[a-1])
        if b>=len(B):
            while c<len(C):
                A[a]=C[c]
                a=a+1
                c=c+1
        if c>=len(C):
            while b<len(B):
                A[a]=B[b]
                a=a+1
                b=b+1
        print("A: ",A)
        return count+linversion+rinversion

A=[3,2,4,1,9,7,10,5]
n=len(A)-1
print(no_inversions(A))
