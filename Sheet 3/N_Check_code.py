# N. Check Code
a,b = map(int, input().split())
s = input()
for i in range(len(s)):
    if i == a and s[i] != "-":
        print("No")
        break
    elif i != a and s[i].isdigit() == False:
        print("No")
        break
else:
    print("Yes")