def repeatedString(s, n):
    ca=0
    size=len(s)
    print("size of string org:",size)
    for i in s:
        if i=='a':
            ca=ca+1
    print("count of a in s: ",ca)
    total=ca*(int(n/size))
    print("total without end substring:", total)
    if not n%size==0:
        s_size=n%size
        ss=s[:s_size]
        print("end substring:", ss, "size of substring:",s_size)
        for i in ss:
            if i=='a':
                total=total+1
    return total

n=549382313570
s='epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq'
print(repeatedString(s, n))