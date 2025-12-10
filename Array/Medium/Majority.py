def majority(n):
    for i in range(len(n)):
        count=0
        for j in range(i,len(n)):
            if n[i]==n[j]:
                count+=1
            if count>=len(n)//2:
                return n[i]

print(majority(n=[1,1,2]))