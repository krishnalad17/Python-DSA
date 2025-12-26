def maxnesting(s):
    maxi=0
    counter=0
    for i in range(len(s)-1):
        if s[i]=="(":
            counter+=1
            maxi=max(maxi,counter)
        elif s[i]==")":
            counter-=1
    return maxi

print(maxnesting(s="(1+(2*3)+((8)/4))+1"))