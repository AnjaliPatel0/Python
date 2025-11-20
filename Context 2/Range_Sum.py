#D. Range Sum

t=int(input())

       
def sum(n):
    return n * (n + 1) // 2
for i in range(t):
        l,r=map(int,input().split())
        if l > r  :
           l,r=r,l  
        result = sum(r) - sum(l - 1)
        print(result)

