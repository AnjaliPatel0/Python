#E. Lowest Number
n=int(input())
a=list(map(int,input().split()))
min=a[0]
pos=1
for i in range(1,n):
    if a[i]<min:
      min=a[i]
      pos=i+1      
    
print(min, pos)
