# P. Minimize Number

n = int(input())
a = list(map(int, input().split()))

count = 0
while True:
    # Check if all numbers are even
    even_num = True
    for x in a:
        if x % 2 != 0:
           even_num = False
           break

    if not even_num:
        break

    # If all even, divide all by 2
    for i in range(n):
        a[i] //= 2

    count += 1

print(count)

