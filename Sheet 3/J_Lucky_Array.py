#J. Lucky Array
n=int(input())
a=list(map(int,input().split()))
minimum = a[0]        # assume first element is minimum
count=0
for i in range(1, n):
    if a[i] < minimum:
        count+= a[i]
if count%2==0:
    print("Unlucky")
else:
    print("Lucky")        
