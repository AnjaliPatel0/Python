#M.Lucky Numbers


A, B = map(int, input().split())
found = False

for num in range(A, B + 1):
    is_lucky = True
    x = num

    while x > 0:
        digit = x % 10
        if digit != 4 and digit != 7:
            is_lucky = False
            break
        x //= 10

    if is_lucky:
        print(num, end=" ")
        found = True

if not found:
    print(-1)