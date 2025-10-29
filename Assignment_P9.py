"""
Cakes
"""
t = int(input())
ans = [None] * t
for i in range(t):
    ans[i] = int(input())
    ans[i] = (ans[i] // 2) + 1
for i in range(t):
    print(ans[i])