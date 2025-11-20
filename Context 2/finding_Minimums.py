#C. Finding Minimums
n,k=map(int,input().split())
m=list(map(int,input().split()))
for i in range(0,n,k):
      c=m[i:i+k]
      print(min(c),end=" ")
    