#X. Convert To Decimal 2
t = int(input())
for _ in range(t):
    n = int(input())
    temp = n
    count = 0
    while temp != 0:
        if temp % 2 == 1:
            count += 1
        temp //= 2
    ans = 0
    base = 2
    power = 0
    for i in range(count):
        ans += (base ** power)
        power += 1
    print(ans)