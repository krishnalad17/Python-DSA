def KadanesAlgorithm(n):
    maxi=float('-inf')
    sum=0

    for i in range (len(n)):
        sum+=n[i]

        if sum>maxi:
            maxi=sum
        if sum<0:
            sum=0
    return print(maxi)

KadanesAlgorithm(n=[2, 3, 5, -2, 7, -4])