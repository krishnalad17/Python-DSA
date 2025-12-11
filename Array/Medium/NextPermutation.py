from itertools import permutations

def nextpermutation(n):
    perm=sorted(set(permutations(n)))

    current=tuple(n)

    for i in range(len(n)):
        if perm[i]==current:
            if i==len(n)-1:
                return perm[0]
            return perm[i+1]

print(nextpermutation(n=[1,3,2]))