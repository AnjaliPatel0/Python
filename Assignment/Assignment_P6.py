def reverse(num):
    res = 0
    while num > 0:
        res = ((res * 10) + (num % 10))
        num //= 10
    return res

# n = int(input("Enter a number: "))
n = int(input())
ans = [None] * n
for i in range(n):
    a,b = map(int, input().split())
    x = reverse(a)
    y = reverse(b)
    z = reverse(x + y)
    ans[i] = z
    
for i in range(n):
    print(ans[i])