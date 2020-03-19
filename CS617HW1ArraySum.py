def array_sum(A,s):
    left=0
    right=len(A)-1
    while(left<right):
        sum=A[left]+A[right]
        if sum<s:
            left=left+1
        elif sum>s:
            right=right-1
        else:
            return True
    return False

def array_sum_recursive(A,s,l,r):
    sum=A[l]+A[r]
    if l==r:
        return False
    elif sum<s:
        return array_sum_recursive(A,s,l+1,r)
    elif sum>s:
        return array_sum_recursive(A,s,l,r-1)
    else:
        return True


A=[0,0,5,7,8,9,10]
#print(array_sum(A,0))
print(array_sum_recursive(A,0,0,len(A)-1))