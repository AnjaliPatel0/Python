#M.Lucky Numbers
a,b=map(int,input().split())
lucky=[4,7,47,744]
found=False
for i in range (a,b+1):
    if i in lucky:
        print(i)
        found= True
if not found:
        print("-1") 