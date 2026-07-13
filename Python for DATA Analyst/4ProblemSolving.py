"""write a program to display a person's name,age 
and address in three lines
"""

name="Anjali"
age=21
Address="634 Nehru nagar"
print(name )
print(age)
print(Address)


#write a program to swap two variables

a=67
b=38
print(a)
print(b)

#first method
"""temp=a
print(temp)

a=b
print(a)

b=temp
print(b)"""

#second method
a,b=b,a
print("After swap")
print(a)
print(b)

#Write a program to convert a float into integer
print("Convert float to integer")
X= 12.4
print(type(X))
X=int(X)
print(type(X))

"""Write a program to take details from a student for
Id-Card and then print it in differrent lines"""

print(" Create Student Identity Card")
name=input("Enter your name:")
age=int(input("Enter your age:"))
roll_no=input("Enter your roll no.: ")
email=input("Enter your email ")

print("Name:", name)
print("Age: ",age)
print("RollNO: ",roll_no)
print("Email:",email)

