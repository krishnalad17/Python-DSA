def pow(x,n):
    if n==0 or x==1:
        return 1
    temp=n
    if n<0:
        x=1/x
        temp=-1*n
    ans=1
    for i in range(temp):
        if n%2==1:
            ans*=x
        x*=x
        n//=2
    return ans


def recursivepow(x,n):
    if n==0:
        return 1
    
    if n<0:
        return 1/recursivepow(x,-n)
    
    half=recursivepow(x,n//2)

    if n%2==0:
        return half*half
    else:
        return x*half*half

print(recursivepow(x=2,n=10))
