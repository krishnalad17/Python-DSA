def NCR(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res

def pascals(n,r):
    for i in range(r):
        print(NCR(n-1,i-1))

print(pascals(n=4,r=5))
            