#The last two Digits
a, b, c, d = map(int, input().split())
result = ((a % 100) * (b % 100) * (c % 100) * (d % 100)) % 100
if(result<10):
 print("0"+str(result))
else:
 print(result)