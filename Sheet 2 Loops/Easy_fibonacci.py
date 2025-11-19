#Y.Easy fibonacci
n=int(input()) 
a=0
b=1
for i in range(n):
    if i == 0:
        print(i,end=" ")
    elif i == 1:
        print(i,end=" ")
    else:
        c=a+b
        a=b
        b=c
        print(c,end=" ")       