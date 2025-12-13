def rotate(n):
    rows=len(n)
    cols=len(n[0])
    for i in range(rows):
        for j in range(i,cols):
            n[i][j],n[j][i]=n[j][i],n[i][j]

    for i in range(rows):
        n[i].reverse()
    return n

print(rotate(n=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
