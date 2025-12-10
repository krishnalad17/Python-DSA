def linearsearch(n,k):
    for i in range(len(n)):
        if n[i]==k:
            return i
    return -1
    
n=[1,5,1,3]
print(linearsearch(n,k=2))