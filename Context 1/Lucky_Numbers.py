#I. Lucky Numbers
n = int(input())

a = n // 10      #tens
b = n % 10       #ones     

if b != 0 and a % b == 0:
    print("YES")
elif a != 0 and b % a == 0:
    print("YES")
else:
    print("NO")