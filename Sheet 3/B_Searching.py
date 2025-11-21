#B. Searching

n = int(input())
nums = input()
lst = list(map(int, nums.split()))
x = int(input())
for i in range(len(lst)):
    if lst[i] == x:
        print(i)
        break
else:
    print(-1)