def method1(n):
    n.sort()
    return n[-2],n[1]

def method2(n):

    if len(n)<=1:
        print(-1,-1)
    
    small=float('inf')
    sec_small=float('inf')
    large=float('-inf')
    sec_large=float('-inf')

    for i in n:
        small=min(small,i)
        large=max(large,i)
    
    for i in n:
        if small<i<sec_small:
            sec_small=i
        if sec_large<i<large:
            sec_large=i

    return sec_large,sec_small

n=[-1,-5,-1,-2,-3]
print(method2(n))