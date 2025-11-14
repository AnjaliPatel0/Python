#D.Ali Baba and Puzzles
A,B,C,D=map(int,input().split())
if A+B-C==D:
    print("YES")
elif A-B+C==D:
    print("YES") 
elif A+B*C==D:
    print("YES")
elif A*B+C==D:
    print("YES")
elif A*B-C==D:
    print("YES") 
elif A-B*C==D:
    print("YES")
else:
    print("NO")
                  
    