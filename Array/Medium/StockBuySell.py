def Stock(n):
    maxi=0
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            prices=n[j]-n[i]
            maxi=max(prices,maxi)
    return maxi

print(Stock(n=[7,1,5,3,6,4]))