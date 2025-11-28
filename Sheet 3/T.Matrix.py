#T. Matrix
n=int(input())
matrix=[]
for _ in range(n):
     row=list(map(int,input().split()))
     matrix.append(row)
     
sum=0
sum1=0
for i in range(n):
    for j in range(i,n):
        if i==j :
            sum=sum+matrix[i][j]

    #for secondary daigonal
    sum1=sum1+matrix[i][n-1-i] 

#for absolute difference
result=abs(sum-sum1)
print(result)

   
