def rotateright(n,k):
    if len(n)==0:
        return
    temp=n[-k:]
    for i in range(len(n)-1-k,-1,-1):
        n[i+k]=n[i]
    
    for i in range(k):
        n[i]=temp[i]
    return n

def rotateleft(n,k):
    if len(n)==0:
        return
    temp=n[:k]
    for i in range(k,len(n)):
        n[i-k]=n[i]  
    for i in range(k):
        n[len(n)-k+i]=temp[i]
    return n




n=[1,5,1,2,3]
print(rotateleft(n,k=2))


