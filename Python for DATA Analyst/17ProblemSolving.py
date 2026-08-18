# 1. Write a program to get Fibonacci series up to 10 numbers
a=0
b=1
n= int(input("enter a number here:"))
if n==1:
    print(1)
else:    
    print(a)
    print(b)
    for i in range(2,n):
      c=a+b
      a=b
      b=c
      print(c,end=" ")





# 2. Write a program to check if a number is prime or not
num=int(input("enter a number here:"))

if num<=1:
   print("it is not a prime number")
else:
   for i in range(2,num):
      if num%i==0:
         print("it is not a prime number") 
         break 
      else:
         print("it is a prime number") 
         break




# 3. Write to find palindrome of integers.
Num=int(input("Enter a string here:"))
rev=0
temp=Num
while Num >0:
     dig = Num%10
     rev=rev*10 + dig
     Num = Num //10
if rev==temp:
   print("it is a palindrome")
else:
   print("it is not a palindrome")   


# 4. Write a program to create an area calculator.
print("*******AREA CALCULATOR******")
while True:
   print(""" press 1 to get the area of square
   press 2 to get area of Rectangle
   press 3 to get the area of circle
   press 4 to get the area of the triangle""")

   choice= int(input("enter a number between 1-4: "))

   if choice == 1:
      while True:
         side = float(input("enter the length of one side : "))
         area = side**2
         print("area of sqaure is ", area)
         repeat = input("do you want to try again with square? ")
         if repeat == "no":
            break

   if choice == 2:
         while True:
            length = float(input("enter the length of the rectangle : "))
            width = float(input("enter the width of the rectangle : "))
            area = length*width
            print("area of rectangle is ", area)
            repeat = input("do you want to try again with rect? ")
            if repeat == "no":
               break 

   if choice == 3:
         while True:
            radius = float(input("enter the radius of the circle : "))
            area = ((22/7)*(radius**2))
            print("area of circlee is ", area)
            repeat = input("do you want to try again with circle? ")
            if repeat == "no":
               break

   if choice == 4:
            while True:
               base = float(input("enter the base of the rectangle : "))
               height = float(input("enter the height of the rectangle : "))
               area = 0.5*base*height
               print("area of triangle is ", area)
               repeat = input("do you want to try again with triangle? ")
               if repeat == "no":
                  break    
   repeat1=input("do you want to repeat the menu again? ")
   if repeat == "no":
      break
                     