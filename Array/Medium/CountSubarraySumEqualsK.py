def countsubarray(n,k):
    count=0
    for i in range(len(n)):
        sum=0
        for j in range(i,len(n)):
            sum+=n[j]
            if sum==k:
                count+=1
    return count 

print(countsubarray(n=[3, 1, 2, 4],k=6))