#S. Search In Matrix
n,m=map(int,input().split())
matrix=[]
for _ in range(n):
     row=list(map(int,input().split()))
     matrix.append(row)
x=int(input())
found=False
for row in matrix:
     if x in row:
          found=True
          break
if found:
    print("will not take number")
else:
    print("will take number")          