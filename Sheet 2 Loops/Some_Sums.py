#U. Some Sums
n,a,b=map(int,input().split())
ans=0
if a > b:
    a,b = b,a
for i in range(1,n+1):
    sum = 0
    x = i
    while x != 0:
        sum += (x % 10)
        x //= 10
    if sum >= a and sum <= b:
        ans += i
print(ans)
    