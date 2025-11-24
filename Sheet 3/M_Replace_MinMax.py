#M. Replace MinMax
n=int(input())
arr=list(map(int,input().split()))
min=arr[0]
max=arr[0]
min_index=0
max_index=0
for i in range(1,n):
     if arr[i]<min:
          min=arr[i]
          min_index=i
     if arr[i]>max:
          max=arr[i]
          max_index=i
arr[min_index],arr[max_index]=arr[max_index],arr[min_index]

for i in range(n):
     print(arr[i],end=" ")