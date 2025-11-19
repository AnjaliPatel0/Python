#N Numbers Histogram
s=input()
n=int(input())
m=list(map(int,input().split()))
for i in range(n):
    print(s*m[i])
