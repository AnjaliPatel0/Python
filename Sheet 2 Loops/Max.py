#E.Max
N=int(input())
M=list(map(int,input().split()))
max_num=M[0]
for i in M:
    if i > max_num:
        max_num = i
print(max_num)
