#P12.GCD and LCM

T = int(input())  

for _ in range(T):
    X, Y = map(int, input().split())
    for i in range(1, min(X, Y) + 1):
        if X % i == 0 and Y % i == 0:
            gcd = i
    #lcm=(a*b)/gcd
    lcm = (X * Y) // gcd

    print(gcd, lcm)