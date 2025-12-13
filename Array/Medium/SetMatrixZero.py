def setmatrix(n):
    row=len(n)
    col=len(n[0])
     
    zero_row=set()
    zero_col=set()

    for i in range(row):
        for j in range(col):
            if n[i][j]==0:
                zero_row.add(i)
                zero_col.add(j)

    for i in zero_row:
        for j in range(col):
            n[i][j]=0
    
    for j in zero_col:
        for i in range(row):
            n[i][j]=0

    return print(n)




setmatrix(n=[[1,1,1],[1,0,1],[1,1,1]])