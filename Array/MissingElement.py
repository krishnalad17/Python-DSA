def missing(n):
    m=max(n)
    x=min(n)
    lists=[]
    for i in range(x,m):
        if i not in n:
            lists.append(i)
    return lists
    
def missingOnlyOne(n):
    N=len(n)+1
    total_sum=N*(N+1)//2
    arr_sum=sum(n)
    return total_sum-arr_sum

n=[1,2,3,5]
print(missingOnlyOne(n))
