

n = int(input())
ans = [None] * n
for i in range(n):
    sh, sm, eh, em = map(int, input().split())
    start = (sh*60)+sm
    end = (eh*60)+em
    total = end - start
    hour = total // 60
    minute = total % 60
    ans[i] = [hour, minute]
    # print(hour, minute) 
for i in range(n):
    print(ans[i][0], ans[i][1])