#Write a program to check if a number is positive
"""num=int(input("enter a number here:"))

if num>0:
    print("number is positive")
else:
    print("number is negative ") """

#Write a program to check a number is odd or even
"""a=int(input("enter a number"))
if a%2==0:
    print("number is even ") 
else:
    print("number is odd") """ 


#Write a program   tp create area calculator
print("****AREA CALCULATOR****")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle """)  


"""choice=int(input("enter a number from 1-4:"))

if choice == 1:
    side= int(input("enter the side of square:""))
    area= side**2
    print("the area of square is ", area)

elif choice ==2:
    length= float(input("enter the length of the rec:"))
    width= float(input("enter the width of the rectangle:"))
    area=length*width
    print("the area of rectangle is ",area)

elif choice == 3:
    radius= float(input("enter the radius of the circle: "))
    area=(3.14*(radius**2))
    print("area of circle is ", area)  

elif choice == 4:
      base=float(input("Enter the base of the triangle: "))
      height=float(input("Enter the height of the triangle: "))
      area=0.5*base*height
      print("area of triangle is ", area)

else:
    print("invalid input")  """ 


#Write a program check whether the passes letter is a vowel or not
letter ="w"
if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is a vowel")   
else:
    print("it is not  a vowel") 


#Write a program to check if a number is a single digit number
num=4444
if num>=0 and num<=9:
    print("it is a single digit number")
elif num>=10 and num<=99:
    print("it is a double digit number")
elif num>=100 and num<=999:
    print("it is a triple digit number")  
else:
    print("it is a four digit number")          

