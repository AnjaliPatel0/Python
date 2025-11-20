# F. Break number
n=int(input())
m=list(map(int,input().split()))
count=0
 
for i in m:
    sum=0 
    while i%2==0:
        i//=2
        sum+=1
    count=max(count,sum)    
print(count)
