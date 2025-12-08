def gcd(m,n):
    l=min(m,n)
    lists=[]
    for i in range (1,l):
        if m%i==0 and n%i==0:
            lists.append(i)
    return lists[-1]

def lcm(m,n):
    start=max(m,n)

    while True:
        if start%m==0 and start%n==0:
            return start
            break
        start+=1
    
def lcmwithgcd(m,n):
    g=gcd(m,n)
    lcm=m*n/g
    return lcm

print(lcm(12,18))