#P12.GCD and LCM

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
def lcm(a, b, g):
    return (a // g) * b
n = int(input())
ans = [None] * n
for i in range(n):
    a, b = map(int, input().split())
    x = gcd(a, b)
    y = lcm(a, b, x)
    ans[i] = [x, y]
for i in range(n):
    print(ans[i][0], ans[i][1])