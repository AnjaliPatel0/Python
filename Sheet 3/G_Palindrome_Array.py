#G. Palindrome Array
n=int(input())
a=list(map(int,input().split()))

is_pal = True


for i in range(n // 2):
    if a[i] != a[n - 1 - i]:
        is_pal = False
        break

if is_pal:
    print("YES")
else:
    print("NO")      
    