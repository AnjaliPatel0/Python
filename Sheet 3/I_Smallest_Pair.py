#I. Smallest Pair
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=float('inf')
    for i in range(0,n):
        for j in range(i+1,n):
            res = a[i] + a[j] + (j+1) - (i+1)
            if res<ans:
                ans=res
    print(ans)   