#1
#1 2
#1 2 3
#1 2 3 4
#write a program to dipaly this pattern

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    

#1
#2 2
#3 3 3
#4 4 4 4
#write a program to dipaly this pattern  
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


#1 1 1 1
#2 2 2
#3 3 
#4 
#write a program to dipaly this pattern  
for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=" ")
    print()     

#         *         
#      *  *
#   *  *  *
#*  *  *  *
#write a program to dipaly this pattern  
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(i):   
        print("*",end=" ")  
    print()       


#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1 
#write a program to dipaly this pattern  
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print() 

#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*
#write a program to dipaly this pattern   
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print() 
for i in range(5,0,-1):
    for m in range(0,i-1):
        print("*",end=" ")
    print()  

#display a table in triangle pattern
for i in range(1,11):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()                