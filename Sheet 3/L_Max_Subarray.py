#L. Max Subarray

t = int(input())
for _ in range(t):
    n = int(input())
    nums = input()
    nums = list(map(int, nums.split()))
    for i in range(len(nums)):
        for j in range(0,i+1):
            maxEle = nums[j]
            idx = j
            while(idx <= i):
                maxEle = max(maxEle,nums[idx])
                idx+=1
            print(maxEle,end=" ")
    print()