def lcs(n):
    n=set(n)
    long=0

    for i in n:
        if i-1 not in n:
            curr=i
            count=1

            while curr+1 in n:
                count+=1
                curr+=1

            long=max(count,long)
    return long
        

print(lcs(n=[100,4,200,1,3,2]))