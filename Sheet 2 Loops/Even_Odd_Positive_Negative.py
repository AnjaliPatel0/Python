#C.Even, Odd, Positive and Negative
N=int(input())
M=list(map(int,input().split()))
even_count=0
odd_count=0
negative_count=0
positive_count=0
for i in M:
    if i%2==0:
        even_count +=1
    else:
        odd_count +=1
    if i>0:
        positive_count +=1
    elif i<0:
        negative_count +=1
print("Even:",even_count)
print("Odd:",odd_count)
print("Positive:",positive_count)
print("Negative:",negative_count)                    
