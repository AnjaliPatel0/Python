def solve(a, b):
    a = a % 10
    if b == 0:
        return 1
    patterns = []
    currValue = a
    while currValue not in patterns:
        patterns.append(currValue)
        currValue=(currValue*a) % 10
    lastDigit = (b - 1) % len(patterns)
    return patterns[lastDigit]

n = int(input())
ans = [None] * n
for i in range(n):
    a, b = map(int, input().split())
    ans[i] = solve(a, b)
for i in range(n):
    print(ans[i])