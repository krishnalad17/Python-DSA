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



def countgood(n):
    even_count=(n+1)//2
    odd_count=n//2

    return recursivepow(5,even_count) * recursivepow(4,odd_count) 

print(countgood(n=4))