#For loop
for i in range (1,6,2):
    print(i)

#print table
n=12
for i in range(1,11):
    print(n,"*",i,"=",n*i)    

#While loop
N=0
while N<=5:
    print(N)
    N+=1

#while true
""" it is an infinite loop
to break a while true loop,break statement is used
  
while True:
    print("hello")      

while True:
    num1=int(input("enter a number: "))
    num2=int(input("enter another number: "))
    
    print(num1+num2)

    repeat=(input("do you want to stop the program "))
    if repeat=="yes":
        break """

#Nested loop
for i in range(1,4):
    for j in range(1,11):
        print(j, end="")
    print()    

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()  

#for loop with conditional statements
for i in range(1,100):
    if i % 8==0 and i%12==0:
        print(i)          