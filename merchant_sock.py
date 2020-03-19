def merchant_sock(arr,n):
    a=list(set(arr))
    count=0
    for i in a:
        local_count=0
        for j in range(0,n):
            if i==arr[j]:
                local_count=local_count+1
        count=count+int(local_count/2)
    return count

A=[3,2,1,2,3,5,3,7,5,9,10,2,7]
merchant_sock(A,len(A))