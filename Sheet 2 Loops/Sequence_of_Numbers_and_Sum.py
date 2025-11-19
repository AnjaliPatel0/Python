#R. Sequence of Numbers and Sum


def printSum(a,b):
    sum = 0
    for i in range(a,b+1):
        print(i, end=" ")
        sum += i
    print(f"sum ={sum}")
while True:
    a,b = map(int,input().split())
    if a <= 0 or b <= 0:
        break
    if a > b:
        printSum(b,a)
    else:
        printSum(a,b)