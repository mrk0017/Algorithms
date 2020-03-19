def MSI(A,n):
    if n==0:
        return A[n],n,n
    else:
        max_sum,l,r=MSI(A,n-1)
        local_sum=0
        j=n-1
        for i in range(n):
            local_sum=local_sum+A[j]
            if local_sum>max_sum:
                max_sum=local_sum
                l=j
                r=n-1
            j=j-1
        return max_sum,l,r

if __name__ == "__main__":
    A = [2,1,4,-5,-8,-9,10]
    print(MSI(A,len(A)))



