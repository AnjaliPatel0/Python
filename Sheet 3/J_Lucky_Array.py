#J. Lucky Array
n=int(input())
nums=list(map(int,input().split()))

minEle = nums[0]
for i in range(1,n):
    minEle = min(minEle,nums[i])
count = 0
for i in nums:
    if i == minEle:
        count += 1
if count % 2 == 0:
    print("Unlucky")
else:
    print("L" \
    "ucky")     
