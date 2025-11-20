#E. Hady Rides the Train
n=int(input())
row = n // 4
if row % 2 == 0:
    print(n//4,n%4)
else:
    print(n//4,3-(n%4))