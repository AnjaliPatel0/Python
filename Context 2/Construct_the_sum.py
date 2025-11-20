#G. Construct the Sum
t=int(input())
for _ in range(t):
    n,s=list(map(int,input().split()))
    for i in range(n,0,-1):
        for j in range(n-1,0):
        
            if i+j==s:
                print(i,j)
            else:
                print("-1")    
