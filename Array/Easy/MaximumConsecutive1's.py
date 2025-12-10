def maxones(n):
    count=0
    maxi=0
    for i in n:
        if i==1:
            count+=1
        if i==0:
            count=0    
        maxi=max(count,maxi)
    return maxi

n=[1,0,1,1,1,0,1,1,1,1]
print(maxones(n))
