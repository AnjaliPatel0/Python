#I. PalinDrome
N=int(input())
original =N
reverse=0

while N>0:
    A=N%10
    reverse = reverse*10+A
    N=N//10

print(reverse)


if original==reverse:
    print("YES")  
else:
    print("NO")      