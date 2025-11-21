#B. Memo and Momo
A,B,K=map(int,input().split())
if A%K==0 and B%K==0 :
    print("Both")
elif A%K==0 and B%K!=0:
    print("Memo") 
elif A%K!=0 and B%K==0:
    print("Momo") 
elif A%K!=0 and B%K!=0:
    print("No One")                  