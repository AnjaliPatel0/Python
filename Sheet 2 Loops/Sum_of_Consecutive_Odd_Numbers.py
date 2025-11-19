#S. Sum of Consecutive Odd Numbers
n=int(input())
for i in range(1,n+1):
    x,y=map(int,input().split())
    sum=0
    if x > y:
        x,y = y,x
    for i in range(x+1,y):
        if i%2!=0:
            sum+=i
    print(sum)        
