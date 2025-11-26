#P. Minimize Number
t=int(input())
for _ in range(t):
    n=list(map(int,input().split()))
    count=0
    while n>1:
        if n%2==0:
            n//=2
        else:
            n=n-1
        count+=1
    print(count)            