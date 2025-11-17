#H. One Prime
X= int(input())

found = True
if X<=1:
    found=False
else:    
    for i in range(2,X):
        if X%i==0:
          found=False
          
if found:
    print("YES")
else:
    print("NO")        