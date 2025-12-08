def sumofn(n):
    if n==0:
        return 0
    return n + sumofn(n-1)

def factorial(n):
    if n == 0 :
        return 1
    return n * factorial(n-1)

def fibo(n):
    if n<=2:
        return n
    return fibo(n-1) + fibo(n-2)

