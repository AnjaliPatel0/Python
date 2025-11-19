#V. PUM
n=int(input())
num = 1
i = 0
while i < n:
    if num % 4 == 0:
        print("PUM")
        i += 1
    else:
        print(num,end=" ")
    num += 1