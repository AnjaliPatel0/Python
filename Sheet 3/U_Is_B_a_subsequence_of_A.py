#U. Is B a subsequence of A ?

n,m = map(int, input().split())
a = input()
b = input()
a = list(map(int, a.split()))
b = list(map(int, b.split()))
idx1 = 0
idx2 = 0
while idx1 < len(a) and idx2 < len(b):
    if a[idx1] == b[idx2]:
        idx1 += 1
        idx2 += 1
    else:
        idx1 += 1
if idx2 == len(b):
    print("YES")
else:
    print("NO")