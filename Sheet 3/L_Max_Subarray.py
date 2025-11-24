#L. Max Subarray
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    subarray=[]
    for i in range(n):
        for j in range(i,n):
            subarray.append(arr[i:j+1])

        print(subarray)    