#Q. Digits
N=int(input())
for i in range(N):
    a=int(input())

    if a==0:
       print(0)
       continue

    while a>0:
      digit = a%10
      print(digit,end=" ")
      a=a//10
    print()       