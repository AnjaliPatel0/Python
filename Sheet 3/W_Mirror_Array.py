# W. Mirror Array
n,m=map(int,input().split())
matrix=[]
for _ in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
result=[]
for i in range(n):
    temp = []
    for j in range(m-1,-1,-1):
        temp.append(matrix[i][j])
    result.append(temp)
for i in result:
    for j in i:
        print(j,end=" ")
    print()