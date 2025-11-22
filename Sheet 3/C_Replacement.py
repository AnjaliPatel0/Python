#C. Replacement
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]==0:
        print(0,end=" ")
    elif a[i]<0:
        print(2,end=" ")
    else:
        print(1,end=" ")
               