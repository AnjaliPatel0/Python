# Loss in Business
n = int(input())
x = int(input())
ans = [None] * n
for i in range(n):
    skills = int(input())
    if skills >= x:
        ans[i] = "YES"
    else:
        ans[i] = "NO"
for i in range(n):
    print(ans[i])