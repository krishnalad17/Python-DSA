def method1(n):
    n.sort()
    return n[-1]


def method2(n):
    max=n[0]
    for i in n:
        if i>max:
            max=i
    return max

n=[1,5,1,2,3]
print(method2(n))